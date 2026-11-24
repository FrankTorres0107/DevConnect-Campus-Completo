from typing import Optional
from src.domain.entities.vacancy import Vacancy
from src.application.ports.repositories import IVacancyRepository

class PostgresVacancyRepository(IVacancyRepository):
    """
    Implementación concreta para PostgreSQL (ADR-001 y ADR-002).
    Utiliza SELECT ... FOR UPDATE para garantizar cero sobrecupos.
    """
    def __init__(self, db_session):
        self.session = db_session

    def find_by_id_with_lock(self, vacancy_id: str) -> Optional[Vacancy]:
        # Ejemplo de consulta con bloqueo pesimista en PostgreSQL:
        # row = self.session.execute(
        #     "SELECT id, project_id, role_title, available_slots, is_closed "
        #     "FROM vacancies WHERE id = :id FOR UPDATE", {"id": vacancy_id}
        # ).fetchone()
        raise NotImplementedError("Conectar sesión activa de PostgreSQL en producción.")

    def count_by_project(self, project_id: str) -> int:
        raise NotImplementedError("Conectar sesión activa de PostgreSQL en producción.")

    def save(self, vacancy: Vacancy) -> Vacancy:
        raise NotImplementedError("Conectar sesión activa de PostgreSQL en producción.")