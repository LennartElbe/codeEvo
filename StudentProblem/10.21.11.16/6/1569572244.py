import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter (x: int, xs: list) -> list:
    for m in xs:
        if x <= m:
            return list(range(1, m + 1))
        elif x == 0:
            return None
    print(xs)    
       
######################################################################
# Lösung Teil 2. (Test)

print(list_filter(4, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list_filter(7, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list_filter(0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
######################################################################
