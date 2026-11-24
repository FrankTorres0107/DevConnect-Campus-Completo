**ADR 003 — Cómo organizamos el programa por dentro (Monolito Modular):**

* Contexto: Somos un equipo estudiantil con presupuesto gratuito y necesitamos un sistema fácil de mantener.
* Decisión: Construimos un solo servidor bien organizado por secciones internas (Monolito Modular con Clean Architecture), separado de la pantalla web mediante un contrato claro de comunicación.
* Alternativa descartada: Dividir el sistema en muchos servidores pequeños independientes (Microservicios), porque complicaría el mantenimiento y costaría dinero.
* Consecuencia: Es muy barato de operar, rápido de programar y mantiene el código ordenado.



