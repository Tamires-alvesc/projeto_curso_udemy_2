from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://user_user:password_password@93.188.162.196:5234/faculdade"

    class Config:
        case_sensitive = True


settings = Settings()