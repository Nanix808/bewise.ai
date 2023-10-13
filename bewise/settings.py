from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = 'test'
    DB_PASSWORD: str = 'test'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_NAME: str = 'bewise_ai'

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
