from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        # Просто ассинхронная ссылка для подключения к БД
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    @property
    def DATABASE_URL_psycopg(self):
        # Просто ссинхронная ссылка для подключения к БД
        return (f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@"      
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print("ASYNC URL:", settings.DATABASE_URL_asyncpg)