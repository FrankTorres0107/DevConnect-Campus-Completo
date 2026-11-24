from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.project import Project
from src.domain.entities.vacancy import Vacancy
from src.domain.entities.application import Application

class IProjectRepository(ABC):
    @abstractmethod
    def find_by_id(self, project_id: str) -> Optional[Project]:
        pass

    @abstractmethod
    def find_all(self) -> List[Project]:
        pass

    @abstractmethod
    def save(self, project: Project) -> Project:
        pass

class IVacancyRepository(ABC):
    @abstractmethod
    def find_by_id_with_lock(self, vacancy_id: str) -> Optional[Vacancy]:
        """Simula o ejecuta el candado temporal (SELECT FOR UPDATE) para evitar sobrecupos."""
        pass

    @abstractmethod
    def count_by_project(self, project_id: str) -> int:
        pass

    @abstractmethod
    def save(self, vacancy: Vacancy) -> Vacancy:
        pass

class IApplicationRepository(ABC):
    @abstractmethod
    def find_by_id(self, application_id: str) -> Optional[Application]:
        pass

    @abstractmethod
    def exists_active(self, student_id: str, vacancy_id: str) -> bool:
        """Verifica RN-12: Si el alumno ya tiene una solicitud PENDIENTE o ACEPTADA en esa vacante."""
        pass

    @abstractmethod
    def count_pending_by_student(self, student_id: str) -> int:
        """Verifica RN-13: Cuántas solicitudes en espera tiene el alumno."""
        pass

    @abstractmethod
    def save(self, application: Application) -> Application:
        pass