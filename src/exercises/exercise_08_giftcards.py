"""
Exercise 08 — Gift cards

Goal:
- Create a gift card
- Query gift cards
- Disable or adjust gift card (if supported by API/store permissions)
- Store created IDs into SQLite registry using raw SQL
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.storage import repo


def main() -> None:
    settings = load_settings()
    _client = ShopifyGraphQLClient(settings)

    # TODO:
    # - Implement gift card creation mutation (if available)
    # - Query gift cards
    # - Save IDs to SQLite registry
    raise NotImplementedError


if __name__ == "__main__":
    main()
