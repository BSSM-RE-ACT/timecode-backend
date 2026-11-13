from fastapi import APIRouter
from sqlalchemy import text

from app.core.db import engine
from app.core.redis import redis_client

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    """API 생존 확인 (DB·Redis 안 봄 — 컨테이너 헬스체크용)."""
    return {"status": "ok"}


@router.get("/health/deep")
def health_deep() -> dict[str, str]:
    """DB·Redis 연결까지 확인 (운영 탭 /admin/ops/health의 기초)."""
    result = {"api": "ok", "db": "ok", "redis": "ok"}
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception:
        result["db"] = "error"
    try:
        redis_client.ping()
    except Exception:
        result["redis"] = "error"
    return result
