import functools
import typing
import string
import random
import pytest

class Vigenere():
    """"""
    def __init__(self, key):
        """"""
        if key == "":
            raise TypeError("Key darf nicht leer sein")
        else:
            self.key = key

c = Vigenere("ad")
    
