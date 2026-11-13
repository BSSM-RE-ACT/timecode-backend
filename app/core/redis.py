from redis import Redis

from app.core.config import get_settings

redis_client: Redis = Redis.from_url(get_settings().redis_url, decode_responses=True)


def timetable_cache_key(kind: str, entity_id: int | str, week: str) -> str:
    """캐시 키 규칙 (7장): tt:{group|teacher|room}:{id}:{week}"""
    return f"tt:{kind}:{entity_id}:{week}"
