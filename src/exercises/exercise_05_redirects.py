"""
Exercise 05 — Redirects

Goal:
- Create URL redirects in the Shopify store
- Query redirects and verify results
- Store created redirect IDs into SQLite registry using raw SQL
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.storage import repo


def main() -> None:
    settings = load_settings()
    _client = ShopifyGraphQLClient(settings)

    # TODO:
    # - Implement redirectCreate mutation (or equivalent)
    # - Implement redirects query
    # - Save redirect IDs into SQLite registry
    raise NotImplementedError


if __name__ == "__main__":
    main()
