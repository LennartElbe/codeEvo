import functools
import typing
import string
import random
import pytest

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
