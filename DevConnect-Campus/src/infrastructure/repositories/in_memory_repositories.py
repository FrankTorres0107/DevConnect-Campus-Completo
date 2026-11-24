from typing import Optional, List
from src.domain.entities.project import Project
from src.domain.entities.vacancy import Vacancy
from src.domain.entities.application import Application
from src.application.ports.repositories import (
    IProjectRepository,
    IVacancyRepository,
    IApplicationRepository
)

class InMemoryProjectRepository(IProjectRepository):
    def __init__(self):
        # Datos semilla precargados para la demostración en video
        self.db = {
            "proj-1": Project(
                id="proj-1",
                title="Sistema IoT de Monitoreo Ambiental Campus",
                description="Red de sensores universitarios con panel de visualización web.",
                leader_id="est-lider-01",
                status="PUBLICADO"
            ),
            "proj-2": Project(
                id="proj-2",
                title="App de Rutas de Transporte Universitario",
                description="Aplicación móvil para seguimiento de autobuses estudiantiles.",
                leader_id="est-lider-01",
                status="BORRADOR"
            )
        }

    def find_by_id(self, project_id: str) -> Optional[Project]:
        return self.db.get(project_id)

    def find_all(self) -> List[Project]:
        return list(self.db.values())

    def save(self, project: Project) -> Project:
        self.db[project.id] = project
        return project


class InMemoryVacancyRepository(IVacancyRepository):
    def __init__(self):
        # vac-1 tiene solo 1 lugar libre para demostrar en vivo el cierre automático (RN-10)
        self.db = {
            "vac-1": Vacancy(
                id="vac-1",
                project_id="proj-1",
                role_title="Desarrollador Backend Python",
                available_slots=1,
                is_closed=False
            ),
            "vac-2": Vacancy(
                id="vac-2",
                project_id="proj-2",
                role_title="Diseñador UX/UI",
                available_slots=2,
                is_closed=False
            )
        }

    def find_by_id_with_lock(self, vacancy_id: str) -> Optional[Vacancy]:
        return self.db.get(vacancy_id)

    def count_by_project(self, project_id: str) -> int:
        return sum(1 for v in self.db.values() if v.project_id == project_id)

    def save(self, vacancy: Vacancy) -> Vacancy:
        self.db[vacancy.id] = vacancy
        return vacancy


class InMemoryApplicationRepository(IApplicationRepository):
    def __init__(self):
        # Solicitud lista para ser aceptada en la demo
        self.db = {
            "app-1": Application(
                id="app-1",
                vacancy_id="vac-1",
                student_id="est-colab-99",
                status="PENDIENTE"
            )
        }

    def find_by_id(self, application_id: str) -> Optional[Application]:
        return self.db.get(application_id)

    def exists_active(self, student_id: str, vacancy_id: str) -> bool:
        return any(
            a.student_id == student_id
            and a.vacancy_id == vacancy_id
            and a.status in ("PENDIENTE", "ACEPTADA")
            for a in self.db.values()
        )

    def count_pending_by_student(self, student_id: str) -> int:
        return sum(
            1 for a in self.db.values()
            if a.student_id == student_id and a.status == "PENDIENTE"
        )

    def save(self, application: Application) -> Application:
        self.db[application.id] = application
        return application