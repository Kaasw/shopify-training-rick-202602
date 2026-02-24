"""
Exercise 10 — Shopify B2B companies

Goal:
- Create a company
- Add a company contact
- Query company data
- Store created IDs into SQLite registry using raw SQL
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.storage import repo


def main() -> None:
    settings = load_settings()
    _client = ShopifyGraphQLClient(settings)

    # TODO:
    # - Implement companyCreate mutation (if available)
    # - Implement locationCreate mutation (if available)
    # - Implement companyContactCreate or equivalent
    # - Query companies
    # - Save IDs to SQLite registry
    raise NotImplementedError


if __name__ == "__main__":
    main()