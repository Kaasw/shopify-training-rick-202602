from __future__ import annotations
from typing import Any, Dict, Optional

import requests

from src.app.config import Settings


class ShopifyGraphQLClient:
    """
    Shopify Admin GraphQL client (skeleton).

    Trainee tasks:
    - Implement execute()
    - Handle HTTP errors
    - Handle GraphQL top-level 'errors'
    - Return parsed JSON
    """

    def __init__(self, settings: Settings, timeout_seconds: int = 30) -> None:
        self.settings = settings
        self.timeout_seconds = timeout_seconds
        self.endpoint = f"https://{settings.shop_domain}/admin/api/{settings.api_version}/graphql.json"

    def _headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": self.settings.access_token,
        }

    def execute(self, query: str, variables: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a GraphQL operation.

        TODO:
        - POST to self.endpoint with JSON payload {"query": query, "variables": variables}
        - Raise on non-2xx response codes
        - Parse JSON
        - If response contains top-level "errors", raise with details
        - Return parsed JSON
        """
        graph_query = {"query": query, "variables": variables}
        result = requests.post(
            url=self.endpoint,
            headers= self._headers(),
            data=query,
            timeout=30
        )
        return result.json()
        raise NotImplementedError
