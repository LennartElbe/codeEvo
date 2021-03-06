import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
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
        if int(i)+1 <= x:   # Abfangen von reellen, nicht-ganzen Zahlen
            return xs_filt.append(i)
        else:
            return xs_filt
        
######################################################################
# Lösung Teil 2. (Test)

def test_xs_filt():
    xs1 = [1, 0, 2, 3, -1, -5]
    xs2 = [1, 5, 2, 3, 99, 2.5, 3.5]
    assert xs_filt(0, xs1) == [0, -1, -5]
    assert xs_filt(-2, xs1) == [-5]
    assert xs_filt(0, xs2) == []
    assert xs_filt(3, xs2) == [1, 2, 3, 2.5]
    
######################################################################
