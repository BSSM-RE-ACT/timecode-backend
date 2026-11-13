"""권한 체크 뼈대. 실제 JWT 검증은 BE-1(인증) 담당이 채운다."""

from collections.abc import Callable
from typing import Literal

from fastapi import Depends, HTTPException, status

Role = Literal["teacher", "staff", "admin", "super_admin"]


class CurrentUser:
    def __init__(self, id: int, email: str, name: str, roles: list[str]):
        self.id = id
        self.email = email
        self.name = name
        self.roles = roles


def get_current_user() -> CurrentUser:
    # TODO(TCB): Authorization 헤더 / 쿠키의 access JWT 검증
    raise HTTPException(status.HTTP_401_UNAUTHORIZED, "로그인이 필요합니다")


def require_role(*roles: Role) -> Callable[..., CurrentUser]:
    """사용 예: `user = Depends(require_role("admin"))`"""

    def checker(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if not set(roles) & set(user.roles):
            raise HTTPException(status.HTTP_403_FORBIDDEN, "권한이 없습니다")
        return user

    return checker
