import uuid
from src.domain.entities.application import Application
from src.domain.errors.domain_exception import DomainException
from src.application.ports.repositories import (
    IProjectRepository,
    IVacancyRepository,
    IApplicationRepository
)

class ApplyToVacancyUseCase:
    """UC-14: Postularse a una vacante abierta."""

    def __init__(
        self,
        project_repo: IProjectRepository,
        vacancy_repo: IVacancyRepository,
        app_repo: IApplicationRepository
    ):
        self.project_repo = project_repo
        self.vacancy_repo = vacancy_repo
        self.app_repo = app_repo

    def execute(self, student_id: str, vacancy_id: str) -> Application:
        vacancy = self.vacancy_repo.find_by_id_with_lock(vacancy_id)
        if not vacancy:
            raise DomainException("La vacante solicitada no existe.")

        project = self.project_repo.find_by_id(vacancy.project_id)
        if not project:
            raise DomainException("El proyecto no existe.")

        # 1. RN-08: El líder no puede postularse a su propio proyecto
        project.validar_no_autopostulacion(student_id)

        # 2. RN-09 / RN-10: Verificar que haya lugares disponibles
        vacancy.verificar_disponibilidad()

        # 3. RN-12: Evitar solicitudes duplicadas a la misma vacante
        if self.app_repo.exists_active(student_id, vacancy_id):
            raise DomainException("Regla violada (RN-12): Ya tienes una solicitud activa para esta vacante.")

        # 4. RN-13: Máximo 5 solicitudes pendientes por estudiante
        if self.app_repo.count_pending_by_student(student_id) >= 5:
            raise DomainException("Regla violada (RN-13): Has alcanzado el límite máximo de 5 solicitudes pendientes.")

        new_app = Application(
            id=f"app-{uuid.uuid4().hex[:6]}",
            vacancy_id=vacancy_id,
            student_id=student_id,
            status="PENDIENTE"
        )
        return self.app_repo.save(new_app)