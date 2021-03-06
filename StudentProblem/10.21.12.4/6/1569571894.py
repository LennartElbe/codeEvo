import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs:list)-> list:
    """ Die Funktion list_filter prüft in einer Liste alle Elemente die 
        kleiner oder gleich x sind.
        Args:
            int(x): Element zum filtern
            list(xs): Liste mit Elementen
        Return:
            result:  Liste mit allen Elementen kleiner oder gleich x
    
    """
    result = []
    for element in xs:
        if element <= x:
            result.append(element)
    return result
            
            
######################################################################
# Lösung Teil 2. (Test)

assert list_filter(2,[1,2,3,4]) == [1,2]
assert list_filter(2,[-1,25,30, 0]) == [0,-1]
######################################################################
