"""
Exercise 06 — Metafields

Goal:
- Set metafields on products (and optionally customers/orders)
- Query metafields back
- Store created metafield identifiers into SQLite registry using raw SQL (if applicable)
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
    # - Implement metafieldsSet mutation
    # - Query metafields for a product
    # - Save any required identifiers into SQLite
    
    list = [{
      "key": "key 1",
      "namespace": "inventory",
      "ownerId": "gid://shopify/Product/8200201830444",
      "type": MetafieldType.SINGLE_LINE_TEXT_FIELD.value,
      "value": "Hello"
    }]
    
    metafield = {
    "name": "Ingredients",
    "namespace": "bakery",
    "key": "ingredients",
    "description": "A list of ingredients used to make the product.",
    "ownerType": ownerType.PRODUCT.value,
    "type": MetafieldType.SINGLE_LINE_TEXT_FIELD.value
  }
    # print(catalog.create_metafield_definition(metafield))
    
    print(catalog.query_metafield_definitions(ownerType.PRODUCT))
    # raise NotImplementedError


if __name__ == "__main__":
    main()
