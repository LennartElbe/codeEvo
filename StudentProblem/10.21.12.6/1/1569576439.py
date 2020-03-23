import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Function to compute the number of words in a string.
    
    Args:
        s(str): A given string.
        
    Returns:
        r(int): Number of words in the string.
    """

## Lösung Teil 2.
def word_count_iter():
######################################################################
## Lösung Teil 3. (Tests)
[5] Schreiben Sie eine Funktion word_count_iter, die ein iterierbares Argument nimmt, das bei jeder Iteration eine Zeile (einen String) liefert, 
und als Ergebnis ein Tupel aus der Anzahl der Zeilen, der Anzahl der Worte und der Anzahl der Zeichen liefert, die aus dem Argument gelesen worden sind.


def test_word_count_iter():
    testlist1 = ["This is not a test."]
    assert word_count_iter(testlist1) == (1, 5, 15)
    assert word_count_iter() == ()
    assert word_count_iter() == ()
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
