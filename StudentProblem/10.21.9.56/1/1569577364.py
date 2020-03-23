import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str):
    'return the number of words in a given string'
    count = 0
    n = ','
    m = ' '
    for i in s:
        if i == n or i == m:
            count += 1
    return count         
        
## Lösung Teil 2.
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
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    assert next(word_count('ABCD MNOP QRST')) == (1,3,14)
    assert next(word_count('')) == None 
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(filename: f):
    'open a given filename and return a tuple of the numer of the line and the number of words and the number of zeichen in this file '
    with open f as fn:
        for line in f:
            word_count_iter(line)
            
        
######################################################################
