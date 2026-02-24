from __future__ import annotations
from typing import Any, Dict


def ensure_prefix(value: str, prefix: str) -> str:
    """
    Ensure an object name includes the training prefix.
    """
    value = value.strip()
    if value.lower().startswith(prefix.lower()):
        return value
    return f"{prefix}-{value}"


def require_keys(d: Dict[str, Any], keys: list[str]) -> None:
    """
    Simple helper to validate dictionary keys exist.
    """
    missing = [k for k in keys if k not in d]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")