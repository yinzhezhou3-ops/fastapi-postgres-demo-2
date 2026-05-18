import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent


def _required(name: str) -> str:
    """读取必填环境变量，缺失时直接报错退出"""
    value = os.environ.get(name)
    if value is None or value == "":
        print(f"FATAL: missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def _optional(name: str, default: str) -> str:
    """读取可选环境变量，不存在时返回默认值"""
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


# ========== 必填配置 ==========
DATABASE_URL: str = _required("DATABASE_URL")

# ========== 可选配置 ==========
APP_PORT: int = int(_optional("APP_PORT", "8000"))
ENVIRONMENT: str = _optional("ENVIRONMENT", "development")
