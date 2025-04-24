#!/usr/bin/env python3
"""
safe_first_element function
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """first element of a list if it exists"""
    if lst:
        return (lst[0])
    else:
        return (None)
