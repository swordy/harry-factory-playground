"""Application entry point and wiring."""

import subprocess
import time

from fastapi import FastAPI

from app.adapters.http_api import create_health_router
from app.domain.version import Version


def _git_short_sha() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        text=True,
    ).strip()


def create_app(sha: str | None = None, start_time: float | None = None) -> FastAPI:
    """Factory used both by the server and by the test suite.

    Args:
        sha: git short SHA to embed as the version. When *None* (production),
             the real HEAD SHA is resolved via ``git``.
        start_time: ``time.monotonic()`` value representing the application
                    start instant. When *None* (production) it is captured
                    at the time this factory runs, so uptime resets on every
                    fresh server start.
    """
    resolved_sha = sha if sha is not None else _git_short_sha()
    resolved_start = start_time if start_time is not None else time.monotonic()

    version = Version(sha=resolved_sha)

    app = FastAPI()
    app.include_router(create_health_router(version, resolved_start))
    return app


# Entrypoint for `uvicorn app.main:app`
app = create_app()
