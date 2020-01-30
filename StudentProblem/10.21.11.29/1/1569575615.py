import functools
import typing
import string
import random
import pytest

def nwords(s):
    """
    Args:
      s: String
    
      Dieser Funktion zählt die Wörter im Strin s (Wörter sind aus mindestens zwei zeichen ohne ein Leerzeichen gebildet)
    
    Return:
        Int: Anzahl der Wörter"""
    L = list(s)
    H = []
    n = 0
    i = 0
    for j in L:
        if j != " ":
            i += 1
            if i >= 2:
                n += 1
        else:
            i = 0
    if " " not in L and len(L) >= 2:
        n = 1
    return n

def word_count_iter(iterable):
    a = 0
    b = 0
    c = 0
    T = (a, b, c)
    a = len(iterable)
    for i in iterable:
        b += nwords(i)
    for j in iterable:
        c += len(j)
    return a
        
    
