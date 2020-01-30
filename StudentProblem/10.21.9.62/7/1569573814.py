import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """die eine positive ganze Zahl n als Argument nimmt 
    und die Liste aller ihrer Teiler ohne Wiederholung zurückliefert"
    Args: n ist eine Zahl"""
    res = [x for x in range(n) if n % x == 0 ]
    return res

def test_divisors():
    assert divisors(9) == [3,9]
