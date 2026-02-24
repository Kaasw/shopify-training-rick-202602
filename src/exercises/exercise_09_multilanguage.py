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


def main() -> None:
    settings = load_settings()
    _client = ShopifyGraphQLClient(settings)

    # TODO:
    # - Implement translationsRegister mutation (or equivalent)
    # - Query translatable resources
    # - Verify translations were applied
    raise NotImplementedError


if __name__ == "__main__":
    main()
