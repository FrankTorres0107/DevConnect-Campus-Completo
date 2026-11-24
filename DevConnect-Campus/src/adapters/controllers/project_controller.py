from src.application.use_cases.publish_project import PublishProjectUseCase
from src.application.ports.repositories import IProjectRepository
from src.adapters.presenters.dtos import PublishProjectRequestDTO

class ProjectController:
    def __init__(self, publish_use_case: PublishProjectUseCase, project_repo: IProjectRepository):
        self.publish_use_case = publish_use_case
        self.project_repo = project_repo

    def list_all(self) -> list[dict]:
        projects = self.project_repo.find_all()
        return [
            {
                "id": p.id,
                "title": p.title,
                "description": p.description,
                "leader_id": p.leader_id,
                "status": p.status
            }
            for p in projects
        ]

    def publish(self, project_id: str, dto: PublishProjectRequestDTO) -> dict:
        project = self.publish_use_case.execute(project_id=project_id, leader_id=dto.leader_id)
        return {
            "mensaje": "El proyecto ahora es público en la cartelera universitaria.",
            "project_id": project.id,
            "title": project.title,
            "nuevo_estado": project.status
        }