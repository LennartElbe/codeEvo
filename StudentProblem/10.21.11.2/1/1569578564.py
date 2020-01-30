import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> n:
    """ Funktion berechnet zu einem String Argument s die Anzahl der Worte im String.
    args: string
    returns: n
    """
    n = 0
    for i in (len(str)): #looping "abc abc"
        if s[i] is string.whitespace: 
            n+=1 #code fehlerhaft, bei mehreren whitespaces
    return n
    
            
            
        
def word_count_iter(it: iter) -> tuple:
    """ Funktion nimmt iterierbares Argument , das bei jeder Iteration eine Zeile (einen String) liefert
    Funktion liefert als Ergebnis ein Tupel aus der Anzahl der Zeilen, der Anzahl der Worte und der Anzahl der Zeichen, 
    die aus dem Argument gelesen worden sind.
    Args: it iterierbares Objekt
    Returns: t ein Tupel
    """
    t=(,,)
    pass 
