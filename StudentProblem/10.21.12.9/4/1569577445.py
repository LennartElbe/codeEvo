import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere:
    
    def __init__(self, key: str):
        if key == "":
            raise IndexError("The keyword is empty!")
        self.key = key
    
    def encrypt(self, w: str) -> str:
        w_len = len(w)
        keylen = len(self.key)
        keyword = ""
        encrypted = ""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if keylen < w_len:
            keyword = self.key * ((w_len // keylen) + 1)
        else:
            keyword = self.key
        index = 0
        for letter in w:
            alphabet_index = 0
            to_add = 0
            for x in alphabet:
                if keyword[index] == x:
                    to_add = alphabet_index
                    break
                alphabet_index += 1
            encrypted += chr(ord(w[index]) + to_add)
            index += 1
        return encrypted
    
    def decrypt(self, w):
        w_len = len(w)
        keylen = len(self.key)
        keyword = ""
        decrypted = ""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if keylen < w_len:
            keyword = self.key * ((w_len // keylen) + 1)
        else:
            keyword = self.key
        index = 0
        for letter in w:
            alphabet_index = 0
            to_add = 0
            for x in alphabet:
                if keyword[index] == x:
                    to_add = alphabet_index
                    break
                alphabet_index += 1
            decrypted += chr(ord(w[index]) - to_add)
            index += 1
        return decrypted

test = Vigenere("SPAM")
print(test.decrypt("WORLD"))
    
######################################################################
## Lösung Teil 3. (Tests)
def test_Vigenere():
    test = Vigenere("HELLO")
    assert test.encrypt("AAAAA") == "HELLO"
    test = Vigenere("ABC")
    assert test.encrypt("HELLO") == "HFNLP"
    assert test.decrypt("HFNLP") == "HELLO"
    test = Vigenere("SPAM")
    assert test.decrypt("WORLD") == "E@R@2"
    assert test.encrypt("E@R@2") == "WORLD"
######################################################################
