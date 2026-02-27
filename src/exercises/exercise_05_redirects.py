"""
Exercise 05 — Redirects

Goal:
- Create URL redirects in the Shopify store
- Query redirects and verify results
- Store created redirect IDs into SQLite registry using raw SQL
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.storage import repo
from src.shopify.services.catalog import CatalogService

def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    catalog = CatalogService(client)

    # TODO:
    # - Implement redirectCreate mutation (or equivalent)
    # - Implement redirects query
    # - Save redirect IDs into SQLite registry
    
    # redirect = catalog.create_redirect(target="https://skibidi-store-6.myshopify.com/products/the-multi-managd-snowboard",path= "https://skibidi-store-6.myshopify.com/products/the-multi-locatin-snowboard")
    # print(redirect)
    # sent = repo.register_entity("redirect", redirect['urlRedirectCreate']['urlRedirect']['id'])
    # print(sent)
    
    print(catalog.query_redirect(first = 10))
    


if __name__ == "__main__":
    main()
