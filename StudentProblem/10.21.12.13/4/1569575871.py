import functools
import typing
import string
import random
import pytest

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
