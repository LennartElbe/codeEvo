import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Funktion, a Number of Interger and a list of Numbers, 
    to to combine the number and the list in one list"""
    xs = []                 
    try:
        x <= str(xs)
        return xs
    break
                  # returned the list, if the Elements in xs are <= x
    
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter1(x: int, xs: list) -> list:
    assert(list_filter) x = 1

def test_list_filter2(x: int, xs: list) -> list:
    assert(list_filter) x = 1.0
    
def test_list_filter3(x: int, xs: list) -> list:
    assert(list_filter) xs = [1, 2, 3]

def test_list_filter4(x: int, xs: list) -> list:
    assert(list_filter) xs = [(1,2), 4, []]
######################################################################
