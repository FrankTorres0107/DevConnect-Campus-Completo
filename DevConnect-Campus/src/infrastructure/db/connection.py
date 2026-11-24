import os

def get_database_url() -> str:
    """Lee la configuración desde variables de entorno (.env) sin exponer credenciales en el código."""
    return os.getenv("DATABASE_URL", "memory://local-demo")