"""
Exercise 09 — Shopify multi-language

Goal:
- Learn Shopify Translations API concepts
- Add translations for:
  - Product title
  - Collection title
- Query translations to verify
"""

from src.app.config import load_settings
from src.shopify.client import ShopifyGraphQLClient
from src.shopify.services.catalog import CatalogService


def main() -> None:
    settings = load_settings()
    client = ShopifyGraphQLClient(settings)
    catalog = CatalogService(client)

    # TODO:
    # - Implement translationsRegister mutation (or equivalent)
    # - Query translatable resources
    # - Verify translations were applied
    
    
    translations = [
      {
        "locale": "vi",
        "key": "title",
        "value": "Mot cai gi day",
        "translatableContentDigest": "41c9198e970a0c8005e7706600a3fd42e9e41664a6536a6a3f44113b2f7589e5"
      }
    ]
    print(catalog.manual_translate("gid://shopify/Product/8200201830444", translations))
    shop_locale = {
      "published": True
    }
    print(catalog.update_shop_locale("vi", shop_locale))
    
    print(catalog.get_translated_resource("gid://shopify/Product/8200201830444", "vi"))
    


if __name__ == "__main__":
    main()
