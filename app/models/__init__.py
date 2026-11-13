"""모델은 이 패키지에 추가하고 아래에서 import 해야 Alembic이 인식한다 (5장 데이터 모델)."""

from app.models.base import Base

__all__ = ["Base"]
