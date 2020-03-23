import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """ret_list[]: leere Liste, in die die sortierte Liste eingefügt wird. Diese wird zurückgegeben
       Funktion sortiert die Liste entsprechend der Aufgabenstellung    
    """
    ret_list = []
    for i in xs: # geht durch jede Stelle der Eingabeliste
        if i <= x: # falls Listeneintrag i kleiner oder gleich Eingabe x ist, wird i in die Ausgabeliste eingefügt
            ret_list.append(i)
    return ret_list
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter_a():
    a = 3
    b = [1, 2, 3, 4, 5]
    assert list_filter(a, b) == [1, 2, 3]
def test_list_filter_b():
    a = 1
    b = [1, 2, 3, 4, 5]
    assert list_filter(a, b) == [1]
def test_list_filter_c():
    a = 5
    b = [1, 2, 3, 4, 5]
    assert list_filter(a, b) == [1, 2, 3, 4, 5]
def test_list_filter_d():
    a = 0
    b = [1, 2, 3, 4, 5]
    assert list_filter(a, b) == []
def test_list_filter_e():
    a = 8
    b = [1, 2, 3, 4, 5]
    assert list_filter(a, b) == [1, 2, 3, 4, 5]
######################################################################
