import functools
import typing
import string
import random
import pytest

def is_palindromic(n):
    """
    Funktion testet ob eine positive ganze Zahl n>0 ein Palindrom ist.
    Definition Palimdrom: 
    Eine natürliche Zahl ist ein Palindrom, falls die Ziffernfolge ihrerDezimaldarstellung vorwärts und 
    rückwärts gelesen gleich ist.
    
    args:
        n: int (n > 0)
    
    return:
        bool (True, wenn n ein Palimdrom ist False wenn n kein Palimdrom ist)
    """
    if type(n) != int or n <= 0:
        return False
    string_int = str(n)
    compare = []
    compare2 = list(string_int)
    for index in range(len(string_int) - 1, -1, -1):
        compare.append(compare2[index])
    if compare == compare2:
        return True
    else:
        return False
        