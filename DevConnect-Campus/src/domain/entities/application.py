from dataclasses import dataclass
from src.domain.errors.domain_exception import DomainException

@dataclass
class Application:
    id: str
    vacancy_id: str
    student_id: str
    status: str = "PENDIENTE"  # PENDIENTE, ACEPTADA, RECHAZADA, CANCELADA

    def aceptar(self) -> None:
        """RN-17: Solo una solicitud PENDIENTE puede pasar a ACEPTADA."""
        if self.status != "PENDIENTE":
            raise DomainException(f"Regla violada (RN-17): No se puede aceptar una solicitud en estado {self.status}.")
        self.status = "ACEPTADA"