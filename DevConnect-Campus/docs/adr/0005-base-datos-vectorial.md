**ADR 005 — Dónde guardamos la información y cómo hacemos las recomendaciones:**

* Contexto: Necesitamos guardar tanto datos normales (usuarios, proyectos) como las coincidencias de habilidades para el recomendador.
* Decisión: Usamos una sola base de datos (PostgreSQL con la extensión pgvector) que permite guardar tablas tradicionales y además comparar habilidades matemáticas en el mismo lugar, con respaldos diarios.
* Alternativa descartada: Contratar una segunda base de datos externa solo para la inteligencia artificial (más caro y difícil de sincronizar).
* Consecuencia: Ahorro de recursos y menor riesgo de que los datos se desfasen.



