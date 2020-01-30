import functools
import typing
import string
import random
import pytest

def is_palindromic(n):
    zahl_string = str(n)
    zahl_list = list(zahl_string)
    laenge = len(zahl_list)
    teil_a = zahl_list[:(laenge//2)]
    teil_b = zahl_list[(laenge//2):]
    if teil_a == teil_b:
        return True
    else: 
        return False
    
