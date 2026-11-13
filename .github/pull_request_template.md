## 이슈
TCB-

## 변경 내용
-

## 확인
- [ ] `uv run ruff check . && uv run pytest` 통과
- [ ] 마이그레이션이 있으면 `alembic upgrade head` 확인
- [ ] API가 바뀌었으면 `openapi.json` 갱신 (`uv run python scripts/export_openapi.py`)
