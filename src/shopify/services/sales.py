from __future__ import annotations
from typing import Any, Dict

from src.shopify.client import ShopifyGraphQLClient


class SalesService:
    """
    Sales service includes Customers and Orders/Draft Orders.
    Draft orders are recommended for training because direct order creation can be restricted.
    """

    def __init__(self, client: ShopifyGraphQLClient) -> None:
        self.client = client

    def create_customer(self, email: str, first_name: str, last_name: str, phone: str | None = None) -> Dict[str, Any]:
        """
        TODO:
        - Implement customerCreate mutation.
        """
        
        query = """
            mutation ($input: CustomerInput!) {
                customerCreate(input: $input) {
                        userErrors {
                        field
                        message
                    }
                        customer {
                        id
                        email
                        firstName
                        lastName
                        phone
                    }      
                }
            } 
        """
        
        variables = {
            "input" : {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone if phone else None
            }
        }
        
        return self.client.execute(query=query, variables=variables)
        raise NotImplementedError

    def create_order(self, customer_gid: str, variant_gid: str, quantity: int) -> Dict[str, Any]:
        """
        TODO:
        - Implement OrderCreate mutation.
        """
        
        query = """
            mutation ($input: DraftOrderInput!) {
                draftOrderCreate(input: $input) {
                    draftOrder {
                        id
                    }
                }
            }
        """
        
        variables = {
            "input": {
                "purchasingEntity": {
                    "customerId": customer_gid
                },
                "lineItems": {
                    "quantity": quantity,
                    "variantId": variant_gid 
                }
            }
        }
        
        return self.client.execute(query=query, variables=variables)
        
        raise NotImplementedError

    def delete_order(self, draft_order_gid: str) -> Dict[str, Any]:
        """
        TODO:
        - Implement OrderDelete mutation.
        """
        
        query = """
            mutation ($input: DraftOrderDeleteInput!) {
                draftOrderDelete(input: $input) {
                    deletedId
                    userErrors {
                        field
                        message
                    }
                }
            }
        """
        
        variables = {
            "input": {
                "id": draft_order_gid
            }
        }
        return self.client.execute(query=query, variables=variables)
        raise NotImplementedError
