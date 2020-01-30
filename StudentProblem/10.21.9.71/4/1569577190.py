import functools
import typing
import string
import random
import pytest

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
