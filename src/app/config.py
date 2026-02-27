import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """
    Application settings loaded from environment variables.
    """

    shop_domain: str
    api_version: str
    access_token: str
    client_id: str
    client_secret: str
    training_prefix: str
    sqlite_path: str


def load_settings() -> Settings:
    shop_domain = (os.getenv("SHOPIFY_SHOP_DOMAIN") or "").strip()
    api_version = (os.getenv("SHOPIFY_ADMIN_API_VERSION") or "").strip()
    access_token = (os.getenv("SHOPIFY_ADMIN_ACCESS_TOKEN") or "").strip()
    client_id = (os.getenv("SHOPIFY_CLIENT_ID") or "").strip()
    client_secret = (os.getenv("SHOPIFY_CLIENT_SECRET") or "").strip()
    training_prefix = (os.getenv("TRAINING_PREFIX") or "dev-training").strip()
    sqlite_path = (os.getenv("SQLITE_PATH") or "./training.db").strip()

    if not shop_domain or not api_version or not access_token:
        raise RuntimeError(
            "Missing required env vars. Copy .env.sample to .env and fill SHOPIFY_* values."
        )

    return Settings(
        shop_domain=shop_domain,
        api_version=api_version,
        access_token=access_token,
        client_id=client_id,
        client_secret=client_secret,
        training_prefix=training_prefix,
        sqlite_path=sqlite_path,
    )
