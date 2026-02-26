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
    # repo.create_tables()
    custom_collection = catalog.create_custom_collection("Custom Toilet Collection")
    smart_collection = catalog.create_smart_collection("Smart Collection", ruleSet={
        "appliedDisjunctively": False,
        "rules": {
        "column": "TITLE",
        "relation": "CONTAINS",
        "condition": "Snowboard"
        }
      })
    
    custom_data = custom_collection['collectionCreate']['collection']
    smart_data = smart_collection['collectionCreate']['collection']
    repo.upsert_collection(collection_gid=custom_data['id'], title=custom_data['title'])
    repo.upsert_collection(collection_gid=smart_data['id'], title=smart_data['title'])
    
    # raise NotImplementedError

    # Step 2: Create Simple Product and Product with Variants (Assign to collections)
    # TODO:
    # - Use catalog.create_simple_product(...)
    
    simple_product = catalog.create_simple_product("Skibidi Toilet 2.0")
    product_options = [
        {"name": "Color", "values": [
            {"name": "White"}, {"name": "Red"}
        ]},
        
        {"name": "Material", "values": [
            {"name": "Iron"}, {"name": "Wood"}
        ]},
    ]
    # - Use catalog.create_product_with_variants(...)
    variant = catalog.create_product_with_variants(title="Skibidi Toilet with variants", productOptions=product_options)
    
    product_gids = [simple_product['productCreate']['product']['id'], variant['productCreate']['product']['id']]
    print(catalog.add_products_to_collection(collection_gid=custom_data['id'], product_gid=product_gids))
    # - Register created entity IDs into DB registry (repo.register_entity)

    # raise NotImplementedError


if __name__ == "__main__":
    main()
