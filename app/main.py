import os
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings

settings = get_settings()

os.environ["TZ"] = settings.tz
time.tzset()

app = FastAPI(
    title="TimeCode API",
    version="0.1.0",
    description="BSSM 시간표 서비스 타임코드 API",
    # 운영: timecode.bssm.dev/api — 터널이 경로를 그대로 넘기므로 앱이 /api 아래에서 동작
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
