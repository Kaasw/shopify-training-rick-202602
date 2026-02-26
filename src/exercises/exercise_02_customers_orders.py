"""
Exercise 02 — Customers + Draft Orders

Goal:
- Create a customer
- Create a draft order for that customer and one of the created variants
- Save created entity IDs into SQLite registry using raw SQL

Note:
- Draft orders are recommended for training.
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.shopify.services.sales import SalesService
from src.storage import repo


def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    sales = SalesService(client)
    
    # TODO:
    # - Create customer
    customer = sales.create_customer("test@mail.com", "Hieu", "Nguyen")
    print(customer)
    order = sales.create_order("gid://shopify/Customer/9867008606252", "gid://shopify/ProductVariant/45329833230380", 2)
    print(order)
    
    repo.insert_order(order['draftOrderCreate']['draftOrder']['id'])
    # - Read a variant_id from DB (from products table) or query Shopify
    # - Create draft order
    # - Register IDs into DB registry
    # raise NotImplementedError


if __name__ == "__main__":
    main()
