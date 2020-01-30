import functools
import typing
import string
import random
import pytest

class Vigenere:
    """Klasse zur Vignere-Verschlüsselung
    Attributes:key 
    Invariant: key != None
    Notes:
    Gegeben sei ein geheimes Schlüsselwort und ein Klartext (jeweils nur Großbuchstaben).
    Der Schlüssel entsteht durch Vervielfachung des Schlüsselworts, sodassdas Ergebnis mindestens so lang wie der Klartext ist. Derverschlüsselte Text entsteht nun, indem ein Zeichen im Klartext gemäßdem entsprechenden Zeichen im Schlüssel verschoben wird. Dabeientspricht A im Schlüssel einer Verschiebung von 0, B von 1, usw bis Zvon 25. Die Verschiebung erfolgt zyklisch wie bei der Cäsar-Kodierung.
    """
    def __init__(self, key):
        """ Methode initialisiert Klasse mit Paramteter key für Schlüssel
        
        """
        assert key is None, "key cant be none"
        self.key = key
        
    def encrypt(self,w):
        """ Methode encrypt verschlüsselt Text anch Viginere
        Args:
        """
    def decrypt(self,w):
        """ Methode decrypt entschlüsselt Text anch Viginere
        """
        
    
