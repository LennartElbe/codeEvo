import functools
import typing
import string
import random
import pytest

j = 1
k = 1.2
print(k < j)

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
#        if int(i) == i and i <= x:   # Abfangen von reellen, nicht-ganzen Zahlen
        if i <= x:
            print("i:", i, "xs_filt:", xs_filt)
            xs_filt.append(i)
        else:
            print("i:", i, "xs_filt:", xs_filt)
            xs_filt = xs_filt
    return xs_filt


