"""FastAPI application with /health endpoint."""

import os
import time
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Record the process start time at import time so uptime is accurate
_START_TIME: float = time.monotonic()

# Read version from environment variable, falling back to a default
APP_VERSION: str = os.environ.get("APP_VERSION", "1.0.0")

app = FastAPI(title="harry-factory-playground")


@app.get("/health")
def health() -> JSONResponse:
    """Return service health information.

    Returns HTTP 200 with a JSON body containing:
    - status: "ok" (always ok for this lightweight check)
    - version: application version string
    - uptime: seconds since process started (float, rounded to 3 dp)
    - timestamp: ISO 8601 UTC datetime of the response
    """
    uptime_seconds = round(time.monotonic() - _START_TIME, 3)
    body = {
        "status": "ok",
        "version": APP_VERSION,
        "uptime": uptime_seconds,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return JSONResponse(
        content=body,
        status_code=200,
        headers={"Cache-Control": "no-store"},
    )
