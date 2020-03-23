import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """Compute the divisors of a given number and return them as a list.
    Args:
        n (int): A natural number 
    Returns:
        list: The list of divisors of n (without repetition)
    """
    # iterate through every number <= n/2 and check whether the number is a divisor
    # append to list if not in list
    # in the end, append the number
    divs = [n]
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divs.append(i)
    return divs

######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    n1, n2, n3 = 1, 13, 20
    assert divisors(n1) == [1]
    assert divisors(n2) == [13, 1]
    assert divisors(n3) == [20, 1, 2, 4, 5]
    
print(divisors(20))
######################################################################
