from dataclasses import dataclass
from src.domain.errors.domain_exception import DomainException

@dataclass
class Vacancy:
    id: str
    project_id: str
    role_title: str
    available_slots: int
    is_closed: bool = False

    def verificar_disponibilidad(self) -> None:
        """RN-09 y RN-10: Verifica que la vacante siga abierta y con lugares disponibles."""
        if self.is_closed or self.available_slots <= 0:
            raise DomainException("Regla violada (RN-09/RN-10): La vacante está cerrada o ya no tiene lugares disponibles.")

    def decrementar_cupo(self) -> None:
        """RN-09, RN-10 y RN-18: Resta 1 lugar y cierra automáticamente la vacante si llega a 0."""
        self.verificar_disponibilidad()
        self.available_slots -= 1
        if self.available_slots == 0:
            self.is_closed = True