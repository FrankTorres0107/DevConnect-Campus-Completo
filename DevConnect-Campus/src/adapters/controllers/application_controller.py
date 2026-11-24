from src.application.use_cases.apply_to_vacancy import ApplyToVacancyUseCase
from src.application.use_cases.accept_application import AcceptApplicationUseCase
from src.adapters.presenters.dtos import ApplyRequestDTO, AcceptRequestDTO

class ApplicationController:
    """Traduce las peticiones web para los casos de uso de postulaciones."""

    def __init__(
        self,
        apply_use_case: ApplyToVacancyUseCase,
        accept_use_case: AcceptApplicationUseCase
    ):
        self.apply_use_case = apply_use_case
        self.accept_use_case = accept_use_case

    def apply(self, dto: ApplyRequestDTO) -> dict:
        app = self.apply_use_case.execute(
            student_id=dto.student_id,
            vacancy_id=dto.vacancy_id
        )
        return {
            "mensaje": "Postulación registrada con éxito.",
            "application_id": app.id,
            "vacancy_id": app.vacancy_id,
            "student_id": app.student_id,
            "status": app.status
        }

    def accept(self, application_id: str, dto: AcceptRequestDTO) -> dict:
        app, remaining_slots, is_closed = self.accept_use_case.execute(
            application_id=application_id,
            leader_id=dto.leader_id
        )
        return {
            "mensaje": "Candidato aceptado exitosamente en el equipo.",
            "application_id": app.id,
            "nuevo_estado": app.status,
            "cupos_restantes_en_vacante": remaining_slots,
            "vacante_cerrada_automaticamente": is_closed
        }