import functools
import typing
import string
import random
import pytest

def divisors(n: int)->list:
    a = []
    if n < 1:
        return("falscheEingabe")
    for i in range(1,n+1):
        if n%i == 0:
            a += [i]
    return (a)
            
