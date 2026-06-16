"""Application entry point and wiring."""

import subprocess

from fastapi import FastAPI

from app.adapters.http_api import create_version_router
from app.domain.version import Version


def _git_short_sha() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        text=True,
    ).strip()


def create_app(sha: str | None = None) -> FastAPI:
    """Factory used both by the server and by the test suite."""
    resolved_sha = sha if sha is not None else _git_short_sha()
    version = Version(sha=resolved_sha)

    app = FastAPI()
    app.include_router(create_version_router(version))
    return app


# Entrypoint for `uvicorn app.main:app`
app = create_app()
