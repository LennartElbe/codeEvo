import functools
import typing
import string
import random
import pytest

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
def word_count_iter(m):
    """
    Die Funktion word_count_iter
    args:
        m: iterierbares Objekt
    return:
        Tupel aus der Anzahl der Zeilen, der Anzahl der Worte und der Anzahl der Zeichen liefert, die aus dem Argument gelesen worden sind
    """
    zeilen = 0
    worte = nwords(m)
    zeichen = len(m)
    for element in m:
        if element == (" "):
            zeilen += 1
    return (zeilen, worte, zeichen)    
    
    

        
