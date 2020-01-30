import functools
import typing
import string
import random
import pytest

def is_palindromic(n):
    """
        Wandelt int in string, dann string zu list. Danach wird die Länge der Liste
        ermittelt und die Liste in zwei Teile geteilt. Diese Teile werden auf 
        Gleichheit verglichen.
    """
    zahl_string = str(n)
    zahl_list = list(zahl_string)
    laenge = len(zahl_list)
    teil_a = zahl_list[:((laenge//2)-1)]
    teil_b = zahl_list[((laenge//2)-1):]
    if teil_a == teil_b:
        return True
    else: 
        return False
    
