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
######################################################################
## Lösung Teil 3. (Tests)

######################################################################
