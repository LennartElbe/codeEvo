import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
print("Hello World")

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
    print("Start: xs=", xs, "xs_filt=", xs_filt)
    for i in xs:
        print("vor Abfrage: x: ", x, " i:", i, "xs_filt:", xs_filt)
#        if int(i) == i and i <= x:   # Abfangen von reellen, nicht-ganzen Zahlen
        if i <= x:
            print("i:", i, "xs_filt:", xs_filt)
            xs_filt.append(i)
        else:
            print("i:", i, "xs_filt:", xs_filt)
            xs_filt = xs_filt
    return xs_filt


######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    xs1 = [1, 0, 2, 3, -1, -5]
    xs2 = [1, 5, 2, 3, 99, 2.5, 3.5]
    assert list_filter(0, xs1) == [0, -1, -5], "Fall x=0"
    assert list_filter(-2, xs1) == [-5], "Fall x=-2"
    assert list_filter(0, xs2) == [], "Fall: Bedingung fuer kein Element erfuellt"
    assert list_filter(3, xs2) == [1, 2, 3, 2.5], "Fall: reele Zahl groesser x enthalten"
    
######################################################################
