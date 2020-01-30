import functools
import typing
import string
import random
import pytest

def divisors(n)->list:
#gibt alle ganzzahligen Teiler mit  Modulo 0, von 1 bis n in einer Liste  wieder
    teiler = [n]
    if n <= 0:
        return "Ungültige Eingabe"
    else:
        for i in range(1, n):
            if n%i == 0:
                teiler = [teiler] + [i]
    return teiler

        
