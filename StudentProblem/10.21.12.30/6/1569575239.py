import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """ Funktion, die alle Elemente einer Liste
        ausgibt, die kleiner x sind.
        Args:
            x: ganze Zahl
            xs: Liste mit Zahlen
            
        Ergebnis:
            gefilterte Liste
    """
    xs_filt = []
    for i in xs:
        if i <= x:
            xs_filt.append(i)
        else:
            xs_filt = xs_filt
    return xs_filt

