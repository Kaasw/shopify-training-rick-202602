"""
Exercise 06 — Metafields

Goal:
- Set metafields on products (and optionally customers/orders)
- Query metafields back
- Store created metafield identifiers into SQLite registry using raw SQL (if applicable)
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.storage import repo


def main() -> None:
    settings = load_settings()
    _client = ShopifyGraphQLClient(settings)

    # TODO:
    # - Implement metafieldsSet mutation
    # - Query metafields for a product
    # - Save any required identifiers into SQLite
    raise NotImplementedError


if __name__ == "__main__":
    main()
