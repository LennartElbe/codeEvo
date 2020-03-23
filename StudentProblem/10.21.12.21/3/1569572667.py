import functools
import typing
import string
import random
import pytest

def leap(jz: Jahreszahl) -> bool:
    """ leap year wenn durch 4 teilbar, ODER durch 100 und 400 teilbar, wenn 100 aber nicht 400 normales jahr
        jz muss >= 1582 sein
       
    """
    if jz >= 1582:
        if jz // 4 == 0:
            return True
            print(jz, " ist ein Schaltjahr")
        elif jz // 100 == 0:
            if jz // 400 == 0:
                return True
                print(jz, " ist ein Schaltjahr")
            else:
                return False
                print(jz, " ist KEIN Schaltjahr")

######################################################################
## Lösung Teil 2 (Tests)


######################################################################
