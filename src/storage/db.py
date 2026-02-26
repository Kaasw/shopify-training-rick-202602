from __future__ import annotations
from typing import Any, Iterable, Optional, Sequence
import sqlite3

from src.app.config import load_settings


def connect() -> sqlite3.Connection:
    """
    Create a SQLite connection using SQLITE_PATH from env.

    Note:
    - This function intentionally does not create tables.
    - Trainees must write CREATE TABLE statements in repo.py using raw SQL.
    """
    settings = load_settings()
    conn = sqlite3.connect(settings.sqlite_path)
    conn.row_factory = sqlite3.Row
    return conn


def execute(sql: str, params: Optional[Sequence[Any]] = None) -> None:
    """
    Execute a single SQL statement (no return rows).

    Trainees should use this for:
    - CREATE TABLE
    - INSERT / UPDATE / DELETE
    """
    try:    
        with connect() as conn:
            conn.execute(sql, params or [])
            conn.commit()
    except sqlite3.OperationalError as e:
            print ("Failed", e)


def execute_many(sql: str, params_list: Iterable[Sequence[Any]]) -> None:
    """
    Execute a SQL statement against multiple parameter sets.
    """
    
    try:    
        with connect() as conn:
            conn.executemany(sql, params_list)
            conn.commit()
    except sqlite3.OperationalError as e:
            print ("Failed", e)
            
def query_all(sql: str, params: Optional[Sequence[Any]] = None) -> list[sqlite3.Row]:
    """
    Execute a SELECT query and return all rows.
    """
    try:    
        with connect() as conn:
            cur = conn.execute(sql, params or [])
            return cur.fetchall()
    except sqlite3.OperationalError as e:
            print ("Failed", e)


