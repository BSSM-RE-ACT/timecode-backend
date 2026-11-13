# 타임코드 백엔드 (timecode-backend)

BSSM 시간표 서비스 **타임코드** API. FastAPI · SQLAlchemy 2 · PostgreSQL · Alembic · Redis.
프론트(학생·교사 웹, 관리자 웹)는 별도 레포 `timecode-frontend`.

## 빠른 시작

```bash
cp .env.example .env
docker compose up -d          # db, redis, api 실행 → http://localhost:8000/api/docs
```

로컬에서 API만 직접 띄우려면 (db·redis는 compose로):

```bash
docker compose up -d db redis
uv sync
uv run alembic upgrade head
uv run fastapi dev app/main.py   # http://localhost:8000/api/docs
```

## 자주 쓰는 명령

| 하는 일 | 명령 |
| --- | --- |
| 테스트 | `uv run pytest` |
| 린트 / 포맷 | `uv run ruff check . --fix` / `uv run ruff format .` |
| 마이그레이션 생성 | `uv run alembic revision --autogenerate -m "add groups"` |
| 마이그레이션 적용 | `uv run alembic upgrade head` |
| OpenAPI 내보내기 | `uv run python scripts/export_openapi.py` → `openapi.json` |

## 폴더 구조

```
app/
  main.py          FastAPI 앱, CORS, root_path=/api
  core/            설정(config), DB 세션, Redis, 권한(require_role)
  api/routes/      라우터 (health, timetable, auth, admin ...)
  models/          SQLAlchemy 모델 — 새 모델은 models/__init__.py 에 import
  schemas/         Pydantic 요청·응답 스키마
  services/        시간표 생성·검증 등 비즈니스 로직 (단위 테스트 필수)
alembic/           마이그레이션
mcp_server/        양식 맞추기 MCP (4단계)
scripts/           유틸 스크립트
tests/
```

## 규칙

- 서버·DB 시간대는 **Asia/Seoul** 고정 (compose·Dockerfile·DB 접속 옵션에 설정됨)
- 권한 체크는 `Depends(require_role("admin"))`
- API를 바꾸면 `openapi.json`을 갱신해서 같이 커밋 → 프론트가 타입을 다시 생성
- `main` 직접 푸시 금지, PR + 리뷰 1명. 브랜치·PR 제목에 Jira 키 (`feat/TCB-5-timetable-api`)
