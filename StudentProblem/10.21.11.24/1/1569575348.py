import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    """Berechnet die Anzahl der Worte in s
    Arg: s: str
    Return int: Anzahl der Worte
    """
    counter = 0
    word_started = False
    for i in s:
        if i not in string.whitespace:
            if word_started == False:
                word_started = True
                counter = counter + 1
        else:
            if word_started == True:
                word_started = False
    return counter

        
def word_count_iter(i: iter) -> tuple:
    """Nimmt ein iterierbares Objekt aus Strings
       und gibt Tupel aus Zeilen, words und zeichen zurück
       Arg: i: iter
       return tuple: Zeilen, words und zeichen
    """
    lines = 0
    words = 0
    zeichen = 0
    for l in i:
        lines = lines + 1
        words = words + nwords(l)
        for z in l:
            zeichen = zeichen + 1
    return (lines, words, zeichen)
