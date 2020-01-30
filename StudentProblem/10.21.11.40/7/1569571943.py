import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    return [x for x in range(n + 1) if n % x == 0]
