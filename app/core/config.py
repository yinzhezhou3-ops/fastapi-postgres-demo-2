import os
import sys

def _required(name: str) -> str:
    value = os.environ.get(name)
    if value is None or value == "":
        print(f"FATAL: missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value

# 关键变量：DATABASE_URL
DATABASE_URL: str = _required("DATABASE_URL")
APP_PORT: int = int(os.environ.get("APP_PORT", "8000"))