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
    
    def encrypt(w:str):
        l = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
        for i in w:
            ord
######################################################################
## Lösung Teil 3. (Tests)
def test_Vigenere():
    k = "Zallo"
    print(ord(k[0]))
    assert 1 == 0
######################################################################
