import functools
import typing
import string
import random
import pytest

print(4 % 1)
print(4 % 2)
print(4 % 4)

def divisors(n: int) -> list:
    """ Berechnung der Menge von Teilern einer positiven nganzen Zahl 
    """
    if n<=0:
        return
    else:
        list_d = []
        d = 1
        while d <= n:
            if n % d == 0:
                return list_d.append(d)
        
