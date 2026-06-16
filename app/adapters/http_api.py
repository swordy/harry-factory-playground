"""HTTP adapter — FastAPI router for the version endpoint."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.domain.version import Version


def create_version_router(version: Version) -> APIRouter:
    router = APIRouter()

    @router.get("/version")
    def get_version() -> JSONResponse:
        return JSONResponse({"sha": version.sha})

    return router
