import functools
import typing
import string
import random
import pytest

def list_filter (x: int, xs: list) -> list:
    for m in xs:
        if x <= m:
            return list(range(m) +1)
    print(xs)    
       
