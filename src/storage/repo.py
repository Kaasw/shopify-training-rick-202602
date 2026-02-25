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
    
    query = [""" 
        CREATE TABLE IF NOT EXISTS training_products (
            product_gid TEXT PRIMARY KEY,
            title TEXT,
            handle TEXT,
            status TEXT
        );
        """, 
        
        """CREATE TABLE IF NOT EXISTS training_variants (
        variant_gid TEXT PRIMARY KEY,
        product_gid TEXT,
        title TEXT,
        sku TEXT,
        price TEXT,
        inventory_item_gid TEXT
        );""",
        
        """CREATE TABLE IF NOT EXISTS training_locations (
        location_gid TEXT PRIMARY KEY,
        name TEXT
        );""",
        
        """CREATE TABLE IF NOT EXISTS training_entities (
        entity_type TEXT,
        shopify_gid TEXT PRIMARY KEY,
        note TEXT
        );
    """]
    for statement in query:
        execute(statement)
    # raise NotImplementedError


def register_entity(entity_type: str, shopify_gid: str, note: str | None = None) -> None:
    """
    TODO:
    Insert an entity into training_entities registry table using raw SQL.
    """
    data = (entity_type, shopify_gid, note if note else "NULL")
    query = f"""
        INSERT INTO training_entities VALUES {data}
    """
    return execute(query)
    raise NotImplementedError


def list_entities(entity_type: str | None = None) -> list[dict[str, Any]]:
    """
    TODO:
    Select entities from training_entities using raw SQL.
    """
    
    query = f"""
        SELECT * FROM training_entities WHERE entity_type = '{entity_type}'
    """
    
    return [dict(x) for x in query_all(query)]
    raise NotImplementedError


def delete_entity_record(shopify_gid: str) -> None:
    """
    TODO:
    Delete one entity row by shopify_gid.
    """
    
    query = f"""
        DELETE FROM training_entities WHERE shopify_gid = '{shopify_gid}'
    """
    
    return execute(query)
    raise NotImplementedError


def upsert_location(location_gid: str, name: str) -> None:
    """
    TODO:
    Insert or replace a location row.
    """
    
    query = f"""
        INSERT INTO training_locations(location_gid, name) VALUES ('{location_gid}', '{name}')
            ON CONFLICT(location_gid) DO UPDATE SET 'name' = excluded.name
   """
    return execute(query)
    raise NotImplementedError


def get_any_location_gid() -> str:
    """
    TODO:
    Return one location_gid from training_locations.
    Raise if none exists.
    """
    
    query = """
        SELECT * from training_locations LIMIT 1 
        
    """
    result = query_all(query)
    if not result:
        raise Exception("None exists")
    return result[0]["location_gid"]
    raise NotImplementedError


def upsert_product(product_gid: str, title: str, handle: str | None, status: str | None) -> None:
    """
    TODO:
    Insert or replace a product row.
    """
    query = f"""
        INSERT INTO training_products(product_gid, title, handle, status) VALUES ('{product_gid}', '{title}', {f"'{handle}'" if handle else "NULL"}, {f"'{status}'" if status else "NULL"})
            ON CONFLICT(product_gid) DO UPDATE SET 'title' = excluded.title, 'handle' = excluded.handle, 'status' = excluded.status;
    """
    return execute(query)
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
    
    query = f"""
        INSERT INTO training_variants(variant_gid, product_gid, title, sku, price, inventory_item_gid) VALUES ('{variant_gid}', 
        '{product_gid}', 
        {f"'{title}'" if title else "NULL"}, 
        {f"'{sku}'" if sku else "NULL"}, 
        {f"'{price}'" if price else "NULL"},
        {f"'{inventory_item_gid}'" if inventory_item_gid else "NULL"})
            ON CONFLICT(variant_gid) DO UPDATE SET 
            'product_gid' = excluded.product_gid, 
            'title' = excluded.title, 
            'sku' = excluded.sku, 
            'price' = excluded.price,
            'inventory_item_gid' = excluded.inventory_item_gid;
    """
    
    return execute(query)
    raise NotImplementedError


def list_products_with_variants() -> list[dict[str, Any]]:
    """
    TODO:
    Return a joined view:
    - product_gid, product_title
    - variant_gid, inventory_item_gid
    This is used for quantity update and cleanup.
    """
    
    query = """

    """
    raise NotImplementedError


