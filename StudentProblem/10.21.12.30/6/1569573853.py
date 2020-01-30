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
        if int(i) == i and i <= x:   # Abfangen von reellen, nicht-ganzen Zahlen
            print("i:", i)
            return xs_filt.append(i)
        else:
            return xs_filt
        
print(list_filter(0, [1, 0, 2, 3, -1, -5]))

