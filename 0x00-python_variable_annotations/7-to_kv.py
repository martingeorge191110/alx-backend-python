#!/usr/bin/env python3
"""
to_kv function
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """tuple of str and square of second number"""
    return (k, float(v**2))
