import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    'return the number of words in a given string'
    count = 0
    n = ','
    m = ' '
    for i in s:
        if i == n or i == m:
            count += 1
    return count         
        
def word_count_iter(s: str):
    'return a tuple of the numer of the line and the number of words and the number of zeichen for a given string'
    if s == '':
        return None
    else:
        res = ()
        lst_zeichen = [] 
        for i in s:
            lst_zeichen += i
    
        # anzahl_Zeile = for jeder iteration erhöht sich um 1   
        anzahl_zeichen = len(lst_zeichen)
        anzahl_worter = nwords(s)
        yield tuple(zip(anzahl_zeile, anzahl_worter,anzahl_zeichen))
