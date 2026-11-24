from dataclasses import dataclass
from src.domain.errors.domain_exception import DomainException

@dataclass
class Project:
    id: str
    title: str
    description: str
    leader_id: str
    status: str = "BORRADOR"  # BORRADOR, PUBLICADO, ARCHIVADO

    def validar_lider(self, user_id: str) -> None:
        """RN-05 y RN-15: Solo el líder dueño del proyecto puede administrarlo o aceptar alumnos."""
        if self.leader_id != user_id:
            raise DomainException("Acción denegada: Solo el líder del proyecto tiene permiso para esta operación.")

    def validar_no_autopostulacion(self, student_id: str) -> None:
        """RN-08: El líder no puede postularse como candidato a su propio proyecto."""
        if self.leader_id == student_id:
            raise DomainException("Regla violada (RN-08): El líder del proyecto no puede postularse a sus propias vacantes.")

    def publicar(self, total_vacantes: int) -> None:
        """RN-07 y RN-11: Un proyecto necesita al menos 1 vacante para pasar a PUBLICADO."""
        if self.status != "BORRADOR":
            raise DomainException(f"No se puede publicar un proyecto que está en estado {self.status}.")
        if total_vacantes < 1:
            raise DomainException("Regla violada (RN-07): El proyecto debe tener al menos 1 vacante para publicarse.")
        self.status = "PUBLICADO"