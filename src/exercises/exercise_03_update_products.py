"""
Exercise 03 — Update Products data

Goal:
1) Create two products:
   - One simple product (inventory not tracked initially)
   - One product with variants (variant quantity starts at 100)
2) Save created products/variants and required inventory identifiers into SQLite (raw SQL).
3) Update both products:
   - Set quantity to 200 (for both)
   - Update tags
   - Create a new collection and add products to it
   - Update product titles

Rules:
- Prefix created titles with TRAINING_PREFIX
- Do not hardcode Shopify IDs; store and read them from SQLite
- SQL must be written by the trainee in storage/repo.py
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.shopify.services.catalog import CatalogService
from src.storage import repo
from src.shopify.services.catalog import InventoryAdjustmentReason, Name


def main() -> None:
   settings = load_settings()
   client = ShopifyGraphQLClient(settings)
   catalog = CatalogService(client)

   # Step 0: Ensure tables exist
   # TODO: repo.create_tables()
   #  repo.create_tables()
   # Step 1: Get and store one location (needed for inventory quantity updates)
   # TODO:
   # - Call catalog.list_locations()
   # - Pick one location_gid
   # - repo.upsert_location(location_gid, name)
   
   repo.upsert_location("gid://shopify/Location/80988799020"," My Custom Location")


   # Step 2: Create products with required inventory conditions
   # Requirements:
   # - Simple product: inventory not tracked initially
   # - Variant product: at least one variant starts at quantity=100
   #
   # TODO:
   # - Create simple product via catalog.create_simple_product(title, track_quantity=False)
   # - Create variant product via catalog.create_product_with_variants(title, initial_variant_qty=100)
   # - Extract product_gid, variant_gid(s), inventory_item_gid(s)
   # - Store:
   #   - repo.upsert_product(...)
   #   - repo.upsert_variant(...)
   # - Register created entities for cleanup:
   #   - repo.register_entity("product", product_gid, note=...)
   #   - repo.register_entity("collection", collection_gid, ...) when created
   print(catalog.create_simple_product("Quantity test"))
   
   update_data = {
      "cost": 63,
      "tracked": True
   }
   catalog.update_inventory_item("gid://shopify/InventoryItem/47426620063788", update_data)
   print(catalog.activate_inventory("gid://shopify/InventoryItem/47426620063788", "gid://shopify/Location/80988799020", 10))
   
   # Step 3: Update both products
   # - Set quantity to 200 for both products
   #   For the simple product:
   #     - First enable tracking (tracked=True) on its inventory_item_gid
   #     - Then set on-hand quantity to 200
   #   For the variant product:
   #     - Set on-hand quantity to 200 for the target variant inventory_item_gid
   #
   # TODO:
   # - Read location_gid from DB (repo.get_any_location_gid())
   # - Read product+variant+inventory_item IDs from DB (repo.list_products_with_variants())
   # - Call:
   #   - catalog.set_inventory_tracked(inventory_item_gid, True) when needed
   #   - catalog.set_on_hand_quantity(inventory_item_gid, location_gid, 200)
   
      
   print(catalog.set_inventory_item_quantity(inventory_item_gid="gid://shopify/InventoryItem/47426620063788", 
                                                location_gid="gid://shopify/Location/80988799020",
                                                reason=InventoryAdjustmentReason.DAMAGED,
                                                name=Name.AVAILABLE,
                                                referenceDocumentUri="logistics://some.warehouse/take/2023-01/13",
                                                quantity=365))
    

   # Step 4: Update tags and titles for both products
   # TODO:
   # - catalog.update_product_tags(product_gid, tags=[...])
   # - catalog.update_product_title(product_gid, new_title=...)
   
   print(catalog.update_product("gid://shopify/Product/8200201830444", tags = ["Sport", "Winter"], title = "Ex 3 test"))

   # Done in ex 1
   # Step 5: Create a new collection and add the two products to it
   # TODO:
   # - collection = catalog.create_custom_collection(...)
   # - catalog.add_products_to_collection(collection_gid, [product_gid_1, product_gid_2])
   # - repo.register_entity("collection", collection_gid, note="created in exercise_03")



if __name__ == "__main__":
   main()
