"""HTTP adapter — FastAPI router for the health endpoint."""

import time

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.domain.version import Version


def create_health_router(version: Version, start_time: float) -> APIRouter:
    """Return a router exposing GET /health.

    Args:
        version: application version value object.
        start_time: ``time.monotonic()`` value captured at application startup;
                    used to compute uptime without wall-clock drift.
    """
    router = APIRouter()

    @router.get("/health")
    def get_health() -> JSONResponse:
        uptime_seconds = time.monotonic() - start_time
        return JSONResponse(
            {
                "status": "ok",
                "version": version.sha,
                "uptime_seconds": uptime_seconds,
            }
        )

    return router
