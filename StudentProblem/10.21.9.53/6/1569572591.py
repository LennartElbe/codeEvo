import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """ret_list[]: leere Liste, in die die sortierte Liste eingefügt wird. Diese wird zurückgegeben
       Funktion sortiert die Liste entsprechend der Aufgabenstellung    
    """
    ret_list = []
    for i in xs: # geht durch jede Stelle der Eingabeliste
        if i <= x: # falls Listeneintrag i kleiner oder gleich Eingabe x ist, wird i in die Ausgabeliste eingefügt
            ret_list.append(i)
    return ret_list
