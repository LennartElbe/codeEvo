import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere:
    """Represents the Vigenere Verschlüsselung
    Atrributes:
        Key: Schlüsselwort für die Verschlüsselung
    Invariants:
        len(key) > 0
    """
    def __init__(self,key):
        assert len(key) > 0, "Bitte nicht leeres Schlüsselwort eingeben!"
        self.key = key
        
    def decrypt(self, w: string) -> string:
        """Fnction to decrypt the given word
            args: w: string word which gets decrypted
        """
        n = len(self.key)
        s = len(w)
        while n != s:
            n += 1
        new_key = self.key * n
        for i in w:
            pas
    



    def encrypt(self, w: string) -> string:
        """ Function to encrypt the given word
            args: w: string word which gets encrypted
        """
        pass
######################################################################
## Lösung Teil 3. (Tests)

######################################################################
