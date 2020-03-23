import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere:
    def __init__(self, s):
        if len(s) != 0:
            self.Schlüsselwort = s
            key = self.Schlüsselwort
        def encrypt(self, w):
            dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y' : 24, 'Z' : 25}
            L = []
            ret = ""
            for i in self.Schlüsselwort:
                L.append(i)
            H = []
            for j in w:
                H.append(j)
            while len(L) != len(H):
                    L.extend(L)
            J = []
            for p in L:
                J.append(dic[p])
            for u in J:
                ret += u
            return ret            
        def decrypt(self, w):
            dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y' : 24, 'Z' : 25}
            L = list(w)
            ret = ""
            for i in L:
                ret += dic[i]
            return ret
            
            
        
######################################################################
## Lösung Teil 3. (Tests)
def test_Vigenere():
    Schlüssl = Vigenere("AAAABBBB")
    assert(Vigenere("AAAABBBB").encrypt() == "00001111")
    assert(Vigenere("").enrypt() == "")
    assert(Vigenere("0105".decrypt()) == "ABAF")
    assert(Vigenere("".decrypt()) == "")
######################################################################
