"""Settings"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Class Settings"""
    DB_USER: str = 'test'
    DB_PASSWORD: str = 'test'
    DB_HOST: str = 'postgres'
    DB_PORT: int = 5432
    DB_NAME: str = 'bewise_ai'

    @property
    def DATABASE_URL_psycopg(self):
        """URL connect DB"""
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
