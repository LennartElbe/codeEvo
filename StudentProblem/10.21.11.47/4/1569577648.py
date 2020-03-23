import functools
import typing
import string
import random
import pytest

## Lösung Teile 1. und 2.
class Vigenere(keyword:str):
    """
    """
    key = []
    def __init__ (self, key:list):
        """
        Standard init function for Vigenere
        
        Args:
        key:list the key used 
        """
        if keyword:
            self.key = key
        except:
            print("Empty strings are not allowed. Failure.")
            
    def encrypt(w:str) -> str:
        """
        Decrypt a Vigenere.
        
        Args:
        w:str the text to be encrypted
        
        Return:
        temp:str the encrypted text
        """
        temp = ""
        for ch in temp:
            ch = ch + key
            temp.append(ch)
        return temp
    
    def decrypt(w:str) -> str:
        """
        Decrypt a Vigenere.
        
        Args:
        w:str the text to be decrypted
        
        Return:
        temp:str the decrypted text
        """
        temp = ""
        for ch in temp:
            ch = ch - key
            temp.append(ch)
        return temp
        
######################################################################
## Lösung Teil 3. (Tests)
def vigenere_test():
    vig = Vigenere("")
######################################################################
