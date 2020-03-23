import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
print(string.whitespace)
def nwords():
    """
    Funktion die zu einem String Argument s die Anzahl der Worte im String berechnet. 
    Worte sind durch mindestens ein Zeichen aus string.whitespace voneinander getrennt.
    Die Funktion string.split darf nicht verwendet werden.

    args:
        s: str
    
    return:
        n: int (Anzahl der wörter in string s)
    """
    """"counter = 0
    for index in range(len(s)):
        if s[index] is not in string.whitespace 
    for char in s:
        if char not in string.whitespace:
            counter"""
## Lösung Teil 2.
def  word_count_iter(iterable_file):
    """
     Funktion word_count_iter, die ein iterierbares Argument nimmt,
     das bei jeder Iteration eine Zeile (einen String) liefert,
     und als Ergebnis ein Tupel aus der Anzahl der Zeilen, der
     Anzahl der Worte und der Anzahl der Zeichen liefert, die aus
     dem Argument gelesen worden sind.
     
     args:
        iterable: str, tuple, list, gen, iter (iterirbares Objekt)
        
     returns:
        n: iter (Iterator )
     """
    num_lines = 0
    num_chars = 0
    num_words = 0
    for a in next(iterable):
        num_lines += 1
        for chars in a:
            num_chars += 1
        b = [a.split()]
        for x in b:
            num_words += 1
    return (num_lines, num_words, num_chars)
        
  
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter()
    text1 = [["abc a b c"], [], ["a", "a"]]
    a = (n 
         for lines in text1 
         for n in lines
        )
    assert word_count_iter(a) == (2, 6, 8)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
