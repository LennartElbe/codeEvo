import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    div_list = []
    if n < 0:
        print("positivity please!")
