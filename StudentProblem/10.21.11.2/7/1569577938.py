import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n:  int) -> list:
    """ Funktion nimmt ganze Zahl n als Argument 
    und liefert die Liste aller ihrer Teiler ohne Wiederholung zurück.
    Args: int eine positive ganzzahlige Zahl
    Returns: list Liste der Teiler ohne Wiederholung
    """
    l=[]
    if n>0:
        for i in range(1, n):
            if n%i == 0:
                l+=[i]
        return l
    
    else:
        return l 
         
    
    
    
#notes brauche schleife
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(0) == []
    assert divisors(1) == [1]
    assert divisors(8) == [1,2,4,8]
######################################################################
