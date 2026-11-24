**ADR 004 y ADR 006 — Comunicación con límite de espera y Plan B si algo falla:**

* Contexto: Las redes universitarias fallan y los servicios de inteligencia artificial pueden tardar.
* Decisión: El navegador espera máximo 8 segundos por petición. Si falla el recomendador inteligente, el sistema cambia en automático a una lista normal ordenada por fecha. Si la base de datos se satura, la plataforma pasa a "modo lectura" (puedes ver proyectos, aunque esperes unos minutos para postularte).
* Alternativa descartada: Dejar que la pantalla cargue infinitamente o mostrar una página de error en blanco.
* Consecuencia: El estudiante nunca se queda frente a una pantalla trabada.



