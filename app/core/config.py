"""환경변수 설정. 값은 .env 또는 실제 환경변수에서 읽는다 (.env.example 참고)."""

from functools import lru_cache
from typing import Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    env: Literal["local", "dev", "prod", "test"] = "local"
    tz: str = "Asia/Seoul"

    # DB / Redis
    database_url: str = "postgresql+psycopg://timecode:timecode@localhost:5432/timecode"
    redis_url: str = "redis://localhost:6379/0"

    # 인증 (10장 로그인 정책)
    jwt_secret: str = "change-me"
    access_token_minutes: int = 15
    refresh_token_days: int = 14
    google_client_id: str = ""
    google_client_secret: str = ""
    allowed_domain: str = "bssm.hs.kr"
    root_admin_emails: str = ""  # 쉼표 구분

    # 도메인·CORS
    web_origin: str = "http://localhost:5173"
    admin_origin: str = "http://localhost:5174"
    extra_cors_origins: str = ""  # 쉼표 구분

    # 시간표 규칙 (4장)
    max_period: int = Field(default=7, ge=1)

    # rate limit (8장, 분당)
    rate_limit_user_per_min: int = 120
    rate_limit_ip_per_min: int = 1000

    @computed_field  # type: ignore[prop-decorator]
    @property
    def cors_origins(self) -> list[str]:
        extra = [o.strip() for o in self.extra_cors_origins.split(",") if o.strip()]
        return [self.web_origin, self.admin_origin, *extra]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def root_admins(self) -> set[str]:
        return {e.strip().lower() for e in self.root_admin_emails.split(",") if e.strip()}


@lru_cache
def get_settings() -> Settings:
    return Settings()
