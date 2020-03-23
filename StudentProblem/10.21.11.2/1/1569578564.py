import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
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
    
            
            
        
## Lösung Teil 2.
def word_count_iter(it: iter) -> tuple:
    """ Funktion nimmt iterierbares Argument , das bei jeder Iteration eine Zeile (einen String) liefert
    Funktion liefert als Ergebnis ein Tupel aus der Anzahl der Zeilen, der Anzahl der Worte und der Anzahl der Zeichen, 
    die aus dem Argument gelesen worden sind.
    Args: it iterierbares Objekt
    Returns: t ein Tupel
    """
    t=(,,)
    pass 
######################################################################
## Lösung Teil 3. (Tests)
def test_word_counter_iter():
    assert word_count_iter("abc abc") == (,,)
    assert word_count_iter("") == (,,)
    assert word_count_iter("abc abc") == (,,)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f: file) -> tuple:
    """ 
    Funktion word_count nimmt einen Dateinamen f als Argument und liefert als Ergebnis ein Tupel aus der Anzahl der Zeilen, 
    der Anzahl der Worte und der Anzahl der Zeichen , die aus der zugehörigen Datei gelesen worden sind.
    Args: f einen Dateinamen
    Returns: tuple 
    """
    pass
    
######################################################################
