from __future__ import annotations

from pathlib import Path
from typing import TypeAlias, Union

import polars as pl
from polars.plugins import register_plugin_function

from tags_parser._internal import __version__ as __version__

LIB = Path(__file__).parent

IntoExprColumn: TypeAlias = Union[pl.Expr, str, pl.Series]


def pig_latinnify(expr: IntoExprColumn) -> pl.Expr:
    return register_plugin_function(
        args=[expr],
        plugin_path=LIB,
        function_name="pig_latinnify",
        is_elementwise=True,
    )
