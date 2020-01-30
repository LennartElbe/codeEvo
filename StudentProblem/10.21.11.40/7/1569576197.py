import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """
    Determines the divisors of a given number.
    """
    return [x for x in range(1, n + 1) if n % x == 0]
