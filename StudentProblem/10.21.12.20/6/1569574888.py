import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list):
#gibt alle ganzzahligen Zahlen aus der Liste xs aus, die in der Liste und Funktionsparameter xs enthalten sind
    same_or_smaller = []
    for i in xs:
        if i <= x:
            same_or_smaller = [same_or_smaller]+[i]
    print(same_or_smaller)
