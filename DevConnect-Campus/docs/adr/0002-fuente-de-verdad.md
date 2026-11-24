**ADR 002 — Quién tiene la última palabra sobre los datos (Fuente de Verdad):**

* Contexto: Un alumno curioso podría intentar alterar la página en su navegador para abrirse paso en un proyecto lleno.
* Decisión: La base de datos central (PostgreSQL) es la única autoridad. Lo que el alumno ve en su pantalla es solo una vista temporal y toda regla se valida dentro del servidor.
* Alternativa descartada: Confiar en las validaciones hechas en el navegador del usuario.
* Consecuencia: El sistema es seguro frente a trampas, aunque requiere validar cada clic importante en el servidor.



