"""
Exercise 04 — Cleanup

Goal:
- Delete all Shopify entities recorded in SQLite registry
- Delete corresponding rows from the registry
- Optionally clear local training tables

Recommended deletion order:
1) orders
2) products
3) collections
4) customers (if deletion is permitted)

Note:
- Shopify permissions may restrict certain deletions.
- Handle partial failures and log userErrors.
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.shopify.services.catalog import CatalogService
from src.shopify.services.sales import SalesService
from src.storage import repo


def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    catalog = CatalogService(client)
    sales = SalesService(client)

    # TODO:
    print(catalog.delete_product("gid://shopify/Product/8197640585260"))
    print(sales.delete_order("gid://shopify/DraftOrder/1110019571756"))
    # - For each entity type, call the correct delete mutation
    # - repo.delete_entity_record(gid) after successful deletion

if __name__ == "__main__":
    main()
