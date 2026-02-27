"""
Exercise 10 — Shopify B2B companies

Goal:
- Create a company
- Add a company contact
- Query company data
- Store created IDs into SQLite registry using raw SQL
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.shopify.services.catalog import CatalogService
from src.storage import repo


def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    catalog = CatalogService(client)


    # TODO:
    # - Implement companyCreate mutation (if available)
    # - Implement locationCreate mutation (if available)
    # - Implement companyContactCreate or equivalent
    # - Query companies
    # - Save IDs to SQLite registry
    
    # print(catalog.create_company("Skibini"))
    location_data = {
        "locale": "vi",
        "name": "Toilet World"
    }
    # print(catalog.create_company_location("gid://shopify/Company/3882058038", location_data))
    contact_data = {
    "email": "avery.brown@example.com",
    "firstName": "Avery",
    "lastName": "Brown"
  }
    print(catalog.create_company_contact("gid://shopify/Company/3882058038", contact_data))
    
    


if __name__ == "__main__":
    main()