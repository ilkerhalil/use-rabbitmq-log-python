from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    RABBITMQ_HOST : str
    RABBITMQ_PORT : int
    RABBITMQ_USER : str
    RABBITMQ_PASSWORD : str


load_dotenv() # Load .env file
settings = Settings()

def get_rabbitmq_config():
    config = {
        "rabbitmq_user": settings.RABBITMQ_USER,
        "rabbitmq_password": settings.RABBITMQ_PASSWORD,
        "rabbitmq_host": settings.RABBITMQ_HOST,
        "rabbitmq_port": settings.RABBITMQ_PORT
    }

    return config