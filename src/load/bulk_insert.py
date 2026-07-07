from .db_connection import get_connection
from psycopg2.extras import execute_values # type: ignore
from typing import Any


def bulk_insert(query: str, rows: list[tuple[Any, ...]]) -> None:
   with get_connection() as conn:
      with conn.cursor() as cur:
         execute_values(cur, query, rows)
      conn.commit()