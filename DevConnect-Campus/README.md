# DevConnect Campus



Plataforma universitaria que conecta a estudiantes que lideran proyectos académicos o tecnológicos con compañeros de distintas carreras dentro de la facultad de informática (UAQ) que buscan colaborar según sus habilidades, garantizando un proceso de postulación ordenado, recomendaciones inteligentes y cero sobrecupos en las vacantes.



##### **## Equipo**

| Nombre | Expediente | 

| :--- | :--- | :--- |

| \[Torres Landa Arévalo Francisco Javier] | \[3333400] 



##### **## Stack**

\* \*\*Lenguaje:\*\* Python 3.11+ / JavaScript

\* \*\*Frameworks:\*\* FastAPI (Backend) y Vue.js (Frontend)

\* \*\*Base de datos:\*\* PostgreSQL con extensión `pgvector`



##### **## Arquitectura**

!\[Diagrama de Arquitectura](docs/arquitectura.png)



El proyecto sigue \*\*Clean Architecture\*\* dividida en 4 capas dentro de `src/`:

\* `src/domain/`: Contiene las entidades (`Project`, `Vacancy`, `Application`) y las reglas de negocio puras (como evitar lugares negativos). No depende de ninguna librería externa.

\* `src/application/`: Contiene los casos de uso (`AcceptApplicationUseCase`, `ApplyToVacancyUseCase`) y las interfaces abstractas (`ports/`) que definen qué necesita guardar el sistema.

\* `src/adapters/`: Contiene los `controllers/` y `presenters/` (DTOs) que reciben las peticiones de la web y las traducen para los casos de uso.

\* `src/infrastructure/`: Contiene las conexiones reales a PostgreSQL (`repositories/`), la configuración del servidor HTTP (`FastAPI`) y servicios externos.



##### **## Cómo correrlo**

1\. \*\*Requisitos:\*\* Python 3.11+, PostgreSQL 15+ (opcional para pruebas en memoria).

2\. Configurar variables de entorno:

&#x20;  ```bash

&#x20;  cp .env.example .env

