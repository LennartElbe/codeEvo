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
    for d in range(1:n+1): #loop bis n
        if int(n) % int(d) == 0:
            j.append(str(d))
            return j
        else:
            return j
    
