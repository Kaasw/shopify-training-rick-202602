from __future__ import annotations
from typing import Any

# execute/query_all are provided. Trainees must write raw SQL.
from src.storage.db import execute, execute_many, query_all


def create_tables() -> None:
    """
    TODO:
    Create tables using raw SQL.

    Suggested tables:

    1) training_products
       - product_gid TEXT PRIMARY KEY
       - title TEXT
       - handle TEXT
       - status TEXT

    2) training_variants
       - variant_gid TEXT PRIMARY KEY
       - product_gid TEXT
       - title TEXT
       - sku TEXT
       - price TEXT
       - inventory_item_gid TEXT

    3) training_locations
       - location_gid TEXT PRIMARY KEY
       - name TEXT

    4) training_entities (registry for cleanup)
       - entity_type TEXT
       - shopify_gid TEXT PRIMARY KEY
       - note TEXT
    """
    raise NotImplementedError


def register_entity(entity_type: str, shopify_gid: str, note: str | None = None) -> None:
    """
    TODO:
    Insert an entity into training_entities registry table using raw SQL.
    """
    raise NotImplementedError


def list_entities(entity_type: str | None = None) -> list[dict[str, Any]]:
    """
    TODO:
    Select entities from training_entities using raw SQL.
    """
    raise NotImplementedError


def delete_entity_record(shopify_gid: str) -> None:
    """
    TODO:
    Delete one entity row by shopify_gid.
    """
    raise NotImplementedError


def upsert_location(location_gid: str, name: str) -> None:
    """
    TODO:
    Insert or replace a location row.
    """
    raise NotImplementedError


def get_any_location_gid() -> str:
    """
    TODO:
    Return one location_gid from training_locations.
    Raise if none exists.
    """
    raise NotImplementedError


def upsert_product(product_gid: str, title: str, handle: str | None, status: str | None) -> None:
    """
    TODO:
    Insert or replace a product row.
    """
    raise NotImplementedError


def upsert_variant(
    variant_gid: str,
    product_gid: str,
    title: str | None,
    sku: str | None,
    price: str | None,
    inventory_item_gid: str | None,
) -> None:
    """
    TODO:
    Insert or replace a variant row.
    """
    raise NotImplementedError


def list_products_with_variants() -> list[dict[str, Any]]:
    """
    TODO:
    Return a joined view:
    - product_gid, product_title
    - variant_gid, inventory_item_gid
    This is used for quantity update and cleanup.
    """
    raise NotImplementedError