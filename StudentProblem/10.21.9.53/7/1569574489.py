import functools
import typing
import string
import random
import pytest

def divisors(n) -> list:
    """
        ret_list: Leere Liste, in die die Zahlen, durch die n teilbar ist,
        eingetragen werden
        Prüft, durch welche ganzen Zahlen die Eingabe n teilbar ist und gibt diese Zahlen
        in einer Liste zurück.
    """
    ret_list = []
    i = 1
    while (i <= n):
        if (n % i) == 0:
            ret_list.append(i)
        i += 1
    return ret_list
        
