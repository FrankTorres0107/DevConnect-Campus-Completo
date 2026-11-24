**ADR 008 — Dónde vive la aplicación en internet:**

* Contexto: Necesitamos que cualquier profesor o alumno pueda entrar desde su navegador sin instalar nada.
* Decisión: La pantalla visual se aloja en Vercel y el servidor en Render dentro de un contenedor estandarizado (Docker), acompañados de una alarma automática (Sentry) que nos avisa si ocurre un error.
* Alternativa descartada: Correr el proyecto únicamente en una computadora personal.
* Consecuencia: Accesible las 24 horas desde cualquier dispositivo sin costo de servidor.



