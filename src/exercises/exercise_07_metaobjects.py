"""
Exercise 07 — Metaobjects

Goal:
- Create a metaobject definition (if needed)
- Create metaobject entries
- Query metaobjects
- Store created IDs into SQLite registry using raw SQL
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.storage import repo


def main() -> None:
    settings = load_settings()
    _client = ShopifyGraphQLClient(settings)

    # TODO:
    # - Implement metaobjectDefinitionCreate (if needed)
    # - Implement metaobjectCreate
    # - Implement metaobject query
    # - Save IDs to SQLite registry
    raise NotImplementedError


if __name__ == "__main__":
    main()