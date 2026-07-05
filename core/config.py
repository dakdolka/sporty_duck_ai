from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class TelegramSettings(BaseModel):
    token: str


class ApiSettings(BaseModel):
    url: str

class DBSettings(BaseModel):
    database: str
    host: str
    port: str
    user: str
    password: str
    
    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            
    


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_nested_delimiter=".",
    )

    telegram: TelegramSettings
    api: ApiSettings
    db: DBSettings


settings = Settings()