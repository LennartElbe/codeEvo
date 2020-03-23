import functools
import typing
import string
import random
import pytest

def leap(x):
    ''' Variablen:
              x = int: Das Jahr
    returns True oder Falsch
    '''
#x ist des zu Überprüfende Jahr    
    if x // 4:
        if x // 100 and not // 400
            return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_4():
    assert leap(2000) == True
    
def test_5():
    # Test für nicht durch 4 teilbar
    assert leap(2001) == False

def test_6():
    #Test für Teilbar durch 100 aber nicht durch 400
    assert leap(2100) == False

######################################################################
