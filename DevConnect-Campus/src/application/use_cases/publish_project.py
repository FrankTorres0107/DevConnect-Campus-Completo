from src.domain.entities.project import Project
from src.domain.errors.domain_exception import DomainException
from src.application.ports.repositories import IProjectRepository, IVacancyRepository

class PublishProjectUseCase:
    """UC-08: Publicar un proyecto en la cartelera tras verificar sus vacantes."""

    def __init__(self, project_repo: IProjectRepository, vacancy_repo: IVacancyRepository):
        self.project_repo = project_repo
        self.vacancy_repo = vacancy_repo

    def execute(self, project_id: str, leader_id: str) -> Project:
        project = self.project_repo.find_by_id(project_id)
        if not project:
            raise DomainException("El proyecto no existe.")

        project.validar_lider(leader_id)
        total_vacantes = self.vacancy_repo.count_by_project(project_id)
        project.publicar(total_vacantes)

        return self.project_repo.save(project)