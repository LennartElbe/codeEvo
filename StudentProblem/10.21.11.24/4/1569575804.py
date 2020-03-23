import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere():
    """"""
    def __init__(self, key):
        """"""
        if key == "":
            raise TypeError("Key darf nicht leer sein")

c = Vigenere("")
    
######################################################################
## Lösung Teil 3. (Tests)

######################################################################
