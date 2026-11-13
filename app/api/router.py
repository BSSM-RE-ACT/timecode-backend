from fastapi import APIRouter

from app.api.routes import health

api_router = APIRouter()
api_router.include_router(health.router)
# TODO: timetable, auth, admin 라우터를 여기에 추가
