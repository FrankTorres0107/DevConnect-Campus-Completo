from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.domain.errors.domain_exception import DomainException
from src.infrastructure.repositories.in_memory_repositories import (
    InMemoryProjectRepository,
    InMemoryVacancyRepository,
    InMemoryApplicationRepository
)
from src.application.use_cases.apply_to_vacancy import ApplyToVacancyUseCase
from src.application.use_cases.accept_application import AcceptApplicationUseCase
from src.application.use_cases.publish_project import PublishProjectUseCase
from src.adapters.controllers.application_controller import ApplicationController
from src.adapters.controllers.project_controller import ProjectController
from src.adapters.presenters.dtos import (
    ApplyRequestDTO,
    AcceptRequestDTO,
    PublishProjectRequestDTO
)

app = FastAPI(
    title="DevConnect Campus API",
    description="Plataforma Universitaria de Vinculación para Proyectos Estudiantiles (Clean Architecture)",
    version="1.0.0"
)

# =========================================================
# INYECCIÓN DE DEPENDENCIAS (Cableado de Capas)
# =========================================================
project_repo = InMemoryProjectRepository()
vacancy_repo = InMemoryVacancyRepository()
app_repo = InMemoryApplicationRepository()

apply_use_case = ApplyToVacancyUseCase(project_repo, vacancy_repo, app_repo)
accept_use_case = AcceptApplicationUseCase(project_repo, vacancy_repo, app_repo)
publish_use_case = PublishProjectUseCase(project_repo, vacancy_repo)

application_controller = ApplicationController(apply_use_case, accept_use_case)
project_controller = ProjectController(publish_use_case, project_repo)


# Esquemas HTTP de entrada para FastAPI (Capa 4)
class ApplySchema(BaseModel):
    student_id: str = "est-colab-02"
    vacancy_id: str = "vac-1"

class AcceptSchema(BaseModel):
    leader_id: str = "est-lider-01"

class PublishSchema(BaseModel):
    leader_id: str = "est-lider-01"


# =========================================================
# ENDPOINTS HTTP
# =========================================================
@app.get("/projects", tags=["Proyectos"])
def listar_proyectos():
    """Lista los proyectos registrados en la plataforma."""
    return project_controller.list_all()


@app.post("/projects/{project_id}/publish", tags=["Proyectos"])
def publicar_proyecto(project_id: str, body: PublishSchema):
    """UC-08: Pasa un proyecto de BORRADOR a PUBLICADO validando RN-05 y RN-07."""
    try:
        dto = PublishProjectRequestDTO(leader_id=body.leader_id)
        return project_controller.publish(project_id, dto)
    except DomainException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/applications/apply", status_code=201, tags=["Postulaciones y Cupos"])
def postularse_a_vacante(body: ApplySchema):
    """UC-14: Registra la postulación de un alumno validando RN-08, RN-09, RN-12 y RN-13."""
    try:
        dto = ApplyRequestDTO(student_id=body.student_id, vacancy_id=body.vacancy_id)
        return application_controller.apply(dto)
    except DomainException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/applications/{application_id}/accept", tags=["Postulaciones y Cupos"])
def aceptar_postulacion(application_id: str, body: AcceptSchema):
    """UC-16: Acepta a un alumno, descuenta 1 cupo (RN-18) y cierra la vacante si llega a 0 (RN-10)."""
    try:
        dto = AcceptRequestDTO(leader_id=body.leader_id)
        return application_controller.accept(application_id, dto)
    except DomainException as e:
        raise HTTPException(status_code=409, detail=str(e))