"""
Exercise 00 — Onboarding + Products + SQL

Goal:
1) Understand the repo structure and how the GraphQL client works.
2) Create two test products in Shopify:
   - One simple product (no options)
   - One product with variants (Size, Color)
3) Implement a product query to fetch products (including variants).
4) Store queried products into SQLite using raw SQL.

Rules:
- Prefix created titles with TRAINING_PREFIX
- Do not hardcode Shopify IDs
- SQL must be written by the trainee in storage/repo.py
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.shopify.services.catalog import CatalogService
from src.storage import repo


def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    catalog = CatalogService(client)
    # Step 1: Create two test products (Manual)
    # Step 2: Query products
    # TODO:
    # - Implement catalog.query_products(...)
    # - Extract the product fields into a list of dict rows
    # - Print a short summary


    # Step 3: Save queried products to SQLite
    # TODO:
    # - repo.create_tables()
    # - repo.insert_products(rows)
    # - verify with repo.list_products()
    repo.conn
    raise NotImplementedError


if __name__ == "__main__":
    main()
