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
from src.shopify.services.catalog import CatalogService, MetafieldType, ownerType
from src.storage import repo


def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    catalog = CatalogService(client)

    # TODO:
    # - Implement gift card creation mutation (if available)
    # - Query gift cards
    # - Save IDs to SQLite registry
    
    # print(catalog.create_gift_card("gid://shopify/Customer/9871422750764", 362.00, note="Skibidi to u"))
    print(catalog.query_gift_card())
    
    
    




if __name__ == "__main__":
    main()
