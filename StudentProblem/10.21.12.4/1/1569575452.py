import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str)-> int:
    """
    Die Funktion nwords berechenet zu einem String Argument s die Anzahl der Worte im String.
    
    args:
        s(str): Text 
    return:
        Anzahl an Wörter im Text
       
    """
    if len(s) == 0:
        return 0
    result = 1
    for element in s:
        if element == (" "):
            result += 1
    return result
## Lösung Teil 2.
def word_count_iter(m):
    for zahl, element in enumerate(m):
        yield (zahl, element)
######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
