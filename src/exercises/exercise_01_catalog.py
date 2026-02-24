"""
Exercise 01 — Collections

Goal:
- Create a custom collection
- Create a smart collection (if supported by API/store)
- Query collections (optional)
- Save created entity IDs into SQLite registry using raw SQL
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.shopify.services.catalog import CatalogService
from src.storage import repo


def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    catalog = CatalogService(client)

    # Step 1: Create Collections (Custom and Smart)
    # TODO:
    # - Create collections
    # - Register IDs into registry table
    raise NotImplementedError

    # Step 2: Create Simple Product and Product with Variants (Assign to collections)
    # TODO:
    # - Use catalog.create_simple_product(...)
    # - Use catalog.create_product_with_variants(...)
    # - Register created entity IDs into DB registry (repo.register_entity)

    raise NotImplementedError


if __name__ == "__main__":
    main()
