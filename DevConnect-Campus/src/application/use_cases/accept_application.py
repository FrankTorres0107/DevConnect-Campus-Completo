from src.domain.entities.application import Application
from src.domain.errors.domain_exception import DomainException
from src.application.ports.repositories import (
    IProjectRepository,
    IVacancyRepository,
    IApplicationRepository
)

class AcceptApplicationUseCase:
    """UC-16: Aceptar a un candidato descontando el cupo de forma segura."""

    def __init__(
        self,
        project_repo: IProjectRepository,
        vacancy_repo: IVacancyRepository,
        app_repo: IApplicationRepository
    ):
        self.project_repo = project_repo
        self.vacancy_repo = vacancy_repo
        self.app_repo = app_repo

    def execute(self, application_id: str, leader_id: str) -> tuple[Application, int, bool]:
        app = self.app_repo.find_by_id(application_id)
        if not app:
            raise DomainException("La postulación indicada no existe.")

        vacancy = self.vacancy_repo.find_by_id_with_lock(app.vacancy_id)
        if not vacancy:
            raise DomainException("La vacante asociada no existe.")

        project = self.project_repo.find_by_id(vacancy.project_id)
        if not project:
            raise DomainException("El proyecto asociado no existe.")

        # 1. Validar que quien acepta sea el líder del proyecto (RN-15)
        project.validar_lider(leader_id)

        # 2. Descontar cupo en la vacante (RN-09, RN-10, RN-16, RN-18)
        vacancy.decrementar_cupo()

        # 3. Cambiar estado de la solicitud a ACEPTADA (RN-17)
        app.aceptar()

        # 4. Guardar cambios a través de los contratos
        self.vacancy_repo.save(vacancy)
        self.app_repo.save(app)

        return app, vacancy.available_slots, vacancy.is_closed