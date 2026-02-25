from __future__ import annotations
from typing import Any, Dict, Optional, List

from src.shopify.client import ShopifyGraphQLClient


class CatalogService:
    """
    Catalog service includes Products and Collections to keep training code easy to navigate.
    Inventory is intentionally excluded from this template.
    """

    def __init__(self, client: ShopifyGraphQLClient) -> None:
        self.client = client

    # ----------------------
    # Products
    # ----------------------
    def create_simple_product(self, title: str) -> Dict[str, Any]:
        """
        TODO:
        - Implement productCreate for a product without options.
        - Return response JSON.
        """
        
        query = """
        mutation ($input: ProductCreateInput!) {productCreate (product: $input) {
            product {
                id
                title
                }
            userErrors {
            field
            message
            }
        }
    }
    """     
        variables = {
        "input": {
            "title": title
        }
    }
        return self.client.execute(query=query, variables=variables)
        raise NotImplementedError

    def create_product_with_variants(self, title: str, productOptions: List[dict]) -> Dict[str, Any]:
        """
        TODO:
        - Implement productCreate for a product with options (Size, Color) and variants.
        - Return response JSON.
        """
        query = """
        mutation ($input: ProductCreateInput!) {productCreate (product: $input) {
            product {
                id
                title
                options {
                    id
                    name
                    position
                    optionValues {
                        id
                        name
                        hasVariants
                        }
                    }
                }
            userErrors {
            field
            message
            }
        }
    }
    """     
        variables = {
        "input": {
            "title": title,
            "productOptions": productOptions
        }
    }
        return self.client.execute(query=query, variables=variables)

        raise NotImplementedError

    def query_products(self, first: int = 10, query: Optional[str] = None) -> Dict[str, Any]:
        """
        TODO:
        - Implement products query (by first, optional search query).
        - Return response JSON.
        """

        filter_query = """
        query ($first: Int!, $query: String) {
            products(first: $first, query: $query) {
                edges {
                    node {
                        id
                        title
                    }
                }
            }
        }
    """
        variables = {
            "first": first,
            "query": query if query else None
    }

        return self.client.execute(query=filter_query, variables=variables)
        raise NotImplementedError

    def delete_product(self, product_gid: str) -> Dict[str, Any]:
        """
        TODO:
        - Implement productDelete mutation.
        """

        query = """
        mutation ($input: ProductDeleteInput!) {
            productDelete(input: $input) {
            deletedProductId
            userErrors {
                field
                message
                }
            }
        }
    """
        variables = {
            "input": {
                "id": product_gid
            }
        }

        return self.client.execute(query=query, variables=variables)
        raise NotImplementedError

    # ----------------------
    # Collections
    # ----------------------
    def create_custom_collection(self, title: str) -> Dict[str, Any]:
        """
        TODO:
        - Implement collection creation for your API version.
        """

        query = """
    mutation ($input: CollectionInput!) {
        collectionCreate(input: $input) {
                collection {
                id
                title
            }
            userErrors {
                field
                message
            }
        }
    }
"""
        variables = {
            "input": {
                "title": title
            }
        }

        return self.client.execute(query, variables)
        raise NotImplementedError

    def create_smart_collection(self, title: str, ruleSet: dict) -> Dict[str, Any]:
        """
        TODO:
        - Implement smart collection creation (if supported by your API version).
        """
        query = """
        mutation ($input: CollectionInput!) {
            collectionCreate(input: $input) {
                    collection {
                    id
                    title
                }
                userErrors {
                    field
                    message
                }
                collection {
                    id
                    title
                    ruleSet {
                        rules {
                            column
                            condition
                            relation
                        }
                    }
                }
            }
        }
        """
        variables = {
            "input": {
                "title": title,
                "ruleSet": ruleSet
            }
        }
        
        return self.client.execute(query, variables)
        raise NotImplementedError

    def delete_collection(self, collection_gid: str) -> Dict[str, Any]:
        """
        TODO:
        - Implement collection deletion for your API version.
        """
        raise NotImplementedError


