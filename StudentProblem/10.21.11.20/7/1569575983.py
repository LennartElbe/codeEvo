import functools
import typing
import string
import random
import pytest

def divisior(n: int) -> list:
    """Eine Funktion, die alle Dividenten einer positiven,
    ganzen Zahl in einer Liste wiedergibt
    """
    j = [n]
    d > 0
    for d in range(n+1): #loop bis n
        if int(n) % int(d) == 0:
            j.append(str(d))
            return j
        else:
            return j
    
