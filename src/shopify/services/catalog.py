from __future__ import annotations
from typing import Any, Dict, Optional, List
from enum import Enum

from src.shopify.client import ShopifyGraphQLClient

class InventoryAdjustmentReason(Enum):
    CORRECTION = "correction"
    CYCLE_COUNT_AVAILABLE = "cycle_count_available"
    DAMAGED = "damaged"
    MOVEMENT_CREATED = "movement_created"
    MOVEMENT_UPDATED = "movement_updated"
    MOVEMENT_RECEIVED = "movement_received"
    MOVEMENT_CANCELED = "movement_canceled"
    OTHER = "other"
    PROMOTION = "promotion"
    QUALITY_CONTROL = "quality_control"
    RECEIVED = "received"
    RESERVATION_CREATED = "reservation_created"
    RESERVATION_DELETED = "reservation_deleted"
    RESERVATION_UPDATED = "reservation_updated"
    RESTOCK = "restock"
    SAFETY_STOCK = "safety_stock"
    SHRINKAGE = "shrinkage"

class Name(Enum):
    AVAILABLE = "available"
    ON_HAND = "on_hand"
    COMMITTED = "committed"
    RESERVED = "reserved"
    DAMAGED = "damaged"
    SAFETY_STOCK = "safety_stock"
    QUALITY_CONTROL = "quality_control"
    INCOMING = "incoming"

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

    def create_product_with_variants(self, title: str, productOptions: List[dict], quantity: int = 0) -> Dict[str, Any]:
        """
        TODO:
        - Implement productCreate for a product with options (Size, Color) and variants.
        - Return response JSON.
        """
        query = """
        mutation ($input: ProductCreateInput!) {
            productCreate(product: $input) {
                product {
                    id
                    title
                    tracksInventory 
                    variants(first: 1) {
                        nodes {
                            id
                            inventoryItem {
                                id
                            }
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
                        handle
                        status
                    }
                }
            }
        }
    """
        variables = {
            "first": first,
            "query": query if query else None
    }
        data = self.client.execute(query=filter_query, variables=variables)
        
        edges = data.get('products').get('edges')
        if not edges:
            return "No products found"

        product_dict = {
            x['node']['id']: 
            {
            "title": x['node']['title'],
            "handle": x['node']['handle'],
            "status": x['node']['status']
            } for x in edges
        }
        return product_dict
        raise NotImplementedError

    def delete_product(self, product_gid: str) -> Dict[str, Any]:
        """
        TODO:
        - Implement productDelete mutation.
        """

        query = """
        mutation ($id: ID!) {
            productDelete(input: { id: $id } ) {
            deletedProductId
            userErrors {
                field
                message
                }
            }
        }
    """
        variables = {
                "id": product_gid
        }

        return self.client.execute(query=query, variables=variables)
        raise NotImplementedError
    
    def update_product(self, product_gid, **update_data) -> Dict[str,Any]:
        query = """
            mutation ($product: ProductUpdateInput!) {
                productUpdate(product: $product) {
                    product {
                        id
                    }
                    
                    userErrors {
                        field
                        message
                    }
                }
            }
        """
        
        variables = {
            "product" : {
                "id": product_gid,
                **update_data
            }
        }
        
        return self.client.execute(query=query, variables=variables)

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
        
        query = """
        mutation ($id: ID!) {
            collectionDelete(input: { id: $id } ) {
            deletedCollectionId
            userErrors {
                field
                message
                }
            }
        }
    """
        variables = {
                "id": collection_gid
        }

        return self.client.execute(query=query, variables=variables)
        
        raise NotImplementedError

    def add_products_to_collection(self, product_gid: List[str], collection_gid: str) -> Dict[str, Any]:
        query = """
            mutation ($id: ID!, $productIds: [ID!]!) 
                {
                    collectionAddProducts(id: $id, productIds: $productIds) {
                        collection {
                            id
                            title
                            products(first: 5) {
                                nodes {
                                    id
                                    title
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
            "id": collection_gid,
            "productIds": product_gid
        }
        
        return self.client.execute(query=query, variables=variables)
    
    # ----------------------
    # Locations
    # ----------------------
    def add_location(self, address: dict[str], name: str) -> Dict[str, Any]:
        query = """
            mutation ($input: LocationAddInput!) {
                locationAdd(input: $input) {
                    location {
                        id
                        name
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
                "address": address,
                "name": name
            }
        }
        return self.client.execute(query=query, variables=variables)
    
    def list_location(self, first: int = 5) -> List[Dict[str, Any]]:
        query = """
            query ($first: Int!) {
                locations(first: $first) {
                    nodes {
                        id
                        name
                    }
                }
            }
        """
        
        variables = {"first": first}
        
        return self.client.execute(query=query, variables=variables)
    
    # ----------------------
    # Inventory
    # ----------------------
    def activate_inventory(self, inventory_item_gid: str, location_gid: str, quantity: int) -> Dict[str, Any]:
        query = """
            mutation ($inventoryItemId: ID!, $locationId: ID!, $available: Int) {
                inventoryActivate(inventoryItemId: $inventoryItemId, locationId: $locationId, available: $available) {
                    userErrors {
                        field
                        message
                    }
                    
                    inventoryLevel {
                        id
                        quantities (names: ["available"]) {
                            name
                            quantity
                        }
                        item {
                            id
                        }
                        location {
                            id
                        }
                    }
                }
            }
        """
    
        variables = {
        "inventoryItemId":  inventory_item_gid,
        "locationId": location_gid,
        "available": quantity
        }
        
        return self.client.execute(query=query, variables=variables)
  
    def update_inventory_item(self, inventory_item_gid: str, update_data: dict[str, Any]) -> Dict[str, Any]:
        query = """
            mutation ($id: ID!, $input: InventoryItemInput!) {
                inventoryItemUpdate(id: $id, input: $input) {
                    userErrors {
                        field
                        message
                    }
                    
                    inventoryItem {
                        id
                        tracked
                    }
                }
            }
        """
        
        variables = {
            "id": inventory_item_gid,
            "input": update_data
        }
        return self.client.execute(query=query, variables=variables)
    
    def adjust_inventory_item_quantity(self, inventory_item_gid: str, location_gid: str, 
                                       name: Name, 
                                       reason: InventoryAdjustmentReason, 
                                       referenceDocumentUri: str,
                                       quantity: int) -> Dict[str, Any]:
        query = """
            mutation ($input: InventoryAdjustQuantitiesInput!) {
                inventoryAdjustQuantities(input: $input) {
                    userErrors {
                        field
                        message
                    }
                    
                    inventoryAdjustmentGroup {
                        changes {
                            name
                            quantityAfterChange
                        }
                    }
                }
            }
        """
        
        variables = {
            "input": {
                "name": name.value,
                "reason": reason.value,
                "referenceDocumentUri": referenceDocumentUri,
                "changes": [
                    {
                        "delta": quantity,
                        "inventoryItemId": inventory_item_gid,
                        "locationId": location_gid
                    }
                ]
            }
        }
        
        return self.client.execute(query=query, variables=variables)
    
    def set_inventory_item_quantity(self, inventory_item_gid: str, location_gid: str, 
                                       name: Name, 
                                       reason: InventoryAdjustmentReason, 
                                       referenceDocumentUri: str,
                                       quantity: int) -> Dict[str, Any]:
        query = """
            mutation ($input: InventorySetQuantitiesInput!) {
                inventorySetQuantities(input: $input) {
                    userErrors {
                        field
                        message
                    }
                    
                    inventoryAdjustmentGroup {
                        changes {
                            name
                            quantityAfterChange
                        }
                    }
                }
            }
        """
        
        variables = {
            "input": {
                "name": name.value,
                "reason": reason.value,
                "referenceDocumentUri": referenceDocumentUri,
                "quantities": {
                    "inventoryItemId": inventory_item_gid,
                    "locationId": location_gid,
                    "quantity": quantity,
                    "changeFromQuantity": None
                }             
            }
        }
        
        return self.client.execute(query=query, variables=variables)
    
    # ----------------------
    # Redirect
    # ----------------------   
    def create_redirect(self, path: str, target: str) -> Dict[str, Any]:
        query = """
        mutation UrlRedirectCreate($urlRedirect: UrlRedirectInput!) {
            urlRedirectCreate(urlRedirect: $urlRedirect) {
                urlRedirect {
                id
                path
                target
                }
                userErrors {
                field
                message
                }
            }
        }
        """
        
        variables = {
        "urlRedirect": {
            "path": path,
            "target": target
        }
        }
        
        return self.client.execute(query=query, variables=variables)
    
    def query_redirect(self, first: int = 10, query: Optional[str] = None) -> Dict[str, Any]:
        filter_query = """
        query ($first: Int!, $query: String) {
            urlRedirects(first: $first, query: $query) {
                edges {
                    node {
                        id
                        path
                        target
                    }
                }
            }
        }
    """
        variables = {
            "first": first,
            "query": query if query else None
    }
        data = self.client.execute(query=filter_query, variables=variables)
        
        edges = data.get('urlRedirects').get('edges')
        if not edges:
            return "No urls found"

        url_dict = {
            x['node']['id']: 
            {
            "id": x['node']['id'],
            "path": x['node']['path'],
            "target": x['node']['target']
            } for x in edges
        }
        return url_dict
        raise NotImplementedError
        