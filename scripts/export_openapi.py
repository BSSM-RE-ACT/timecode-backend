"""OpenAPI 스키마를 openapi.json으로 내보낸다. 프론트 레포가 이 파일로 타입을 생성한다.

uv run python scripts/export_openapi.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.main import app  # noqa: E402

out = Path(__file__).resolve().parent.parent / "openapi.json"
out.write_text(json.dumps(app.openapi(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {out}")
