import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere:
    def __init__(self , key):
        if key is not None:
            self.key =  key
        else:
            raise AttributeError
    
    #def encrypt(w:str)
######################################################################
## Lösung Teil 3. (Tests)
def test_Vigenere():
    k = "Aallo"
    print(ord(A))
    assert 1 == 0
######################################################################
