"""
Exercise 07 — Metaobjects

Goal:
- Create a metaobject definition (if needed)
- Create metaobject entries
- Query metaobjects
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
    # - Implement metaobjectDefinitionCreate (if needed)
    # - Implement metaobjectCreate
    # - Implement metaobject query
    # - Save IDs to SQLite registry
    
    # definition = [
    #     {
    #         "name": "Name",
    #         "key": "name",
    #         "type": MetafieldType.SINGLE_LINE_TEXT_FIELD.value
    #     },
    #     {
    #         "name": "Bio",
    #         "key": "bio",
    #         "type": MetafieldType.SINGLE_LINE_TEXT_FIELD.value
    #     }
    # ]
    
    # print(catalog.create_metaobject_definition(definition=definition, name="Designer profile", type="designer_profile"))
    
    # fields = [
    #     {
    #         "key": "name",
    #         "value": "Mr Toilet"
    #     }
    # ]
    
    # print(catalog.create_metaobject(fields, "designer_profile"))
    
    # meta_object = "gid://shopify/Metaobject/184017158188"
    
    print(catalog.query_metaobjects("designer_profile"))
    


if __name__ == "__main__":
    main()