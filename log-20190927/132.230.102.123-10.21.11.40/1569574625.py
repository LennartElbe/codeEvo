import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere:
    def __init__(self, key: str):
        """
        Create object with a secret key.
        """
        assert key
        self.key = key
    
    def encrypt(self, w: str) -> str:
        """
        Encrypt the given text with the secret key of the object.
        """
        new_key = self.key * (len(w) // len(self.key) + 1)
        msg = ""
        for i, c in enumerate(w):
            new_c = chr(ord(c) + (ord(new_key[i]) - ord('A')))
            if ord(new_c) > ord('Z'):
                new_c = chr(ord(new_c) - 26)
            msg += new_c
        return msg
                        
    def decrypt(self, w: str) -> str:
        """
        Decrypts the given text with the secret key of the object.
        """
        new_key = self.key * (len(w) // len(self.key) + 1)
        msg = ""
        for i, c in enumerate(w):
            new_c = chr(ord(c) - (ord(new_key[i]) - ord('A')))
            if ord(new_c) < ord('A'):
                new_c = chr(ord(new_c) + 26)
            msg += new_c
        return msg
######################################################################
## hidden code

def mk_coverage():
    covered = set()
    target = set(range(6))
    count = 0
    
    def coverage(func):
        nonlocal covered, target, count
    
        def wrapper(key):
            nonlocal covered, count
            if key == "A":
                covered.add(0)
            elif key != "":
                covered.add(1)
            if len (key) > 1:
                covered.add(2)
                if key == key[0] * len (key):
                    covered.add(4)
                else:
                    covered.add(5)
            if len (key) > 2:
                covered.add (3)
                
            r = func (key)
            count += 1
            return r
        if func == "achieved": return len(covered)
        if func == "required": return len(target)
        if func == "count" : return count
        functools.update_wrapper (wrapper, func)
        return wrapper
    return coverage

coverage = mk_coverage ()

try:
    Vigenere = coverage (Vigenere)
except:
    pass

## Lösung Teil 3. (Tests)
def test_vigenere():
    v1 = Vigenere("MYSECRETKEY")
    assert v1.decrypt(v1.encrypt("TESTFOOBAR")) == "TESTFOOBAR"
    
    v2 = Vigenere("AAA")
    assert v2.encrypt("BBB") == "BBB"
    
    assert Vigenere("ABCD").encrypt("BAR") == "BBU"
######################################################################
## hidden tests
pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])

from inspect import getfullargspec
class TestNames:
    def test_Vigenere (self):
        assert Vigenere
    def test_encrypt(self):
        assert Vigenere.encrypt
        assert 'w' in getfullargspec(Vigenere.encrypt).args
    def test_decrypt(self):
        assert Vigenere.decrypt
        assert 'w' in getfullargspec(Vigenere.decrypt).args

class TestGrades:

    def test_coverage(self):
        assert coverage("achieved") == coverage("required")

    def test_Vigenere_is_a_class(self):
        assert "class" in repr (Vigenere.__wrapped__)

    def test_docstring_present(self):
        assert Vigenere.__doc__ is not None
        assert Vigenere.encrypt.__doc__ is not None
        assert Vigenere.decrypt.__doc__ is not None

    def test_empty_key (self):
        with pytest.raises (Exception):
            assert Vigenere ("")
            
    def test_has_key(self):
        k = "asfdg"
        v = Vigenere(k)
        assert v.key == k

    def test_has_methods(self):
        v = Vigenere("")
        assert v.encrypt
        assert v.decrypt

    def test_identity(self):
        charset = string.ascii_uppercase
        v = Vigenere ("A")
        for i in range (100):
            s = ''.join(random.choice (charset) for j in range (100))
            assert v.encrypt(s) == s
            assert v.decrypt(s) == s

    def test_inverses(self):
        charset = string.ascii_uppercase
        for i in range (100):
            k = ''.join(random.choice (charset) for j in range (random.randrange (1,20)))
            v = Vigenere (k)
            for n in range (10):
                s = ''.join(random.choice (charset) for j in range (100))
                assert v.decrypt(v.encrypt(s)) == s

    def test_shift (self):
        charset = string.ascii_uppercase
        for i in range (100):
            k = random.choice (charset)
            ok = ord (k) - ord ('A')
            v = Vigenere (k * random.randrange (1, 100))
            s = ''.join(random.choice (charset) for j in range (100))
            se = v.encrypt (s)
            assert len (se) == len (s)
            for x, xe in zip (s, se):
                d = (26 + ord (xe) - ord (x)) % 26
                assert d == ok
            sd = v.decrypt (s)
            assert len (sd) == len (s)
            for x, xd in zip (s, sd):
                d = (26 + ord (x) - ord (xd)) % 26
                assert d == ok


