**ADR 001 — Cómo evitamos que dos alumnos ganen el mismo último lugar:**

* Contexto: Si queda una sola vacante, no podemos permitir que por un error de velocidad se acepten dos personas.
* Decisión: Usamos un candado temporal en la base de datos (bloqueo pesimista en PostgreSQL) que atiende una aceptación a la vez.
* Alternativa descartada: Revisar el cupo solo desde la página web (descartado porque es fácil de engañar o fallar si hay mala conexión).
* Consecuencia: Garantía total de cero sobrecupos, a cambio de que la operación tarde unos milisegundos extra.



