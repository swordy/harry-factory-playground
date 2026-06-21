import time
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"

# Record startup time once at module load
_START_TIME = time.monotonic()


@app.get("/health")
def get_health():
    uptime_seconds = time.monotonic() - _START_TIME
    return jsonify(
        {
            "status": "ok",
            "version": VERSION,
            "uptime": uptime_seconds,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )


if __name__ == "__main__":
    app.run()
