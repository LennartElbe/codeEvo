import functools
import typing
import string
import random
import pytest

def is_palindromic(n):
    """ 
    Args:
        n: Int
    
    Dieser Funktion prüft, ob die Zahl n ein palindrom ist
    
    Return: True
            False"""
    L = []
    H = []
    k = len(n)
    for i in len(n):
        L.append(i)
    while k != 0:
        H.append(L[k])
        k -= 1
    if L == H:
        return True
    else:
        return False
    
    
