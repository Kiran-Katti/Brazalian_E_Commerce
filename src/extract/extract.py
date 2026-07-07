import pandas as pd
from pathlib import Path
from typing import Any, Callable

from pandas.io.parsers.readers import TextFileReader


def get_rows(path: str | Path, load_data: Callable[[list[tuple[Any, ...]]], None]) -> None:

   chunks: TextFileReader = pd.read_csv(path, chunksize= 50000)

   for chunk in chunks:
      # chunk: Any = chunk.where(pd.notna(chunk), None)
      rows: list[tuple[Any, ...]] = [tuple(row) for row in chunk.to_numpy()]
      load_data(rows)