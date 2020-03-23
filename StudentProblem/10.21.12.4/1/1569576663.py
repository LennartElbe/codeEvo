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
    """
    Die Funktion word_count_iter
    args:
        m: iterierbares Objekt
    return:
        Tupel aus der Anzahl der Zeilen, der Anzahl der Worte und der Anzahl der Zeichen liefert, die aus dem Argument gelesen worden sind
    """
    zeilen = 1
    worte = nwords(m)
    zeichen = len(m)
    for element in m:
        if element == (" "):
            zeilen += 1
    return (zeilen, worte, zeichen)    
    
    

        
######################################################################
## Lösung Teil 3. (Tests)
assert word_count_iter("Hallo") == (1,1,5)
assert word_count_iter("Hallo world") == (2,2,11)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count():
    pass
######################################################################
