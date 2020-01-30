import functools
import typing
import string
import random
import pytest

def is_palindromic(n):
    """ Funktion testes, ob  eine positive ganze Zahl n>0 ein Palindrom ist.
    Args: n die zu testende Zahl
    Returns: bool, ob 'Bedingung erfüllt ist
    """
    assert n>0 #
    x = str(n) #for iteration
    y = x[-1::-1] #invers
    l = []
    for i in range(0,len(x)): #123
        if x[i] == y[i]:
            l+=[True]
        else:
            l+=[False]
    if all(l)==True:
        return True
    else:
        return False
    
