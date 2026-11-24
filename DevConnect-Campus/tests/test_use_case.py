import unittest
from src.domain.errors.domain_exception import DomainException
from src.infrastructure.repositories.in_memory_repositories import (
    InMemoryProjectRepository,
    InMemoryVacancyRepository,
    InMemoryApplicationRepository
)
from src.application.use_cases.accept_application import AcceptApplicationUseCase
from src.application.use_cases.apply_to_vacancy import ApplyToVacancyUseCase

class TestDevConnectCleanArchitecture(unittest.TestCase):
    def setUp(self):
        self.project_repo = InMemoryProjectRepository()
        self.vacancy_repo = InMemoryVacancyRepository()
        self.app_repo = InMemoryApplicationRepository()
        self.accept_uc = AcceptApplicationUseCase(self.project_repo, self.vacancy_repo, self.app_repo)
        self.apply_uc = ApplyToVacancyUseCase(self.project_repo, self.vacancy_repo, self.app_repo)

    def test_aceptar_candidato_descuenta_cupo_y_cierra_vacante(self):
        """Verifica UC-16, RN-10 y RN-18: Al aceptar el último lugar, el cupo queda en 0 y se cierra."""
        app, slots, is_closed = self.accept_uc.execute("app-1", leader_id="est-lider-01")
        self.assertEqual(app.status, "ACEPTADA")
        self.assertEqual(slots, 0)
        self.assertTrue(is_closed)

    def test_bloquea_autopostulacion_del_lider(self):
        """Verifica RN-08: El líder no puede postularse a su propio proyecto."""
        with self.assertRaises(DomainException):
            self.apply_uc.execute(student_id="est-lider-01", vacancy_id="vac-1")

if __name__ == "__main__":
    unittest.main()