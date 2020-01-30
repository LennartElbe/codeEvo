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
        if int(i)+1 <= x:   # Abfangen von reellen, nicht-ganzen Zahlen
            return xs_filt.append(i)
        else:
            return xs_filt
        
