from __future__ import annotations
from typing import Any, Dict
from dotenv import set_key
from config import Settings, load_settings
import requests

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
    

def get_access_token():
    settings = load_settings()
    url = f"https://{settings.shop_domain}/admin/oauth/access_token"
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
    "grant_type" : "client_credentials",
    "client_id" : settings.client_id,
    "client_secret":settings.client_secret
    }
    
    response = requests.post(url=url, headers=header, data=data, timeout=30)
    response.raise_for_status()
    
    access_token = response.json()['access_token']
    env_path = ".env"
    
    set_key(env_path, "SHOPIFY_ADMIN_ACCESS_TOKEN", access_token)
    return access_token

# get_access_token()
