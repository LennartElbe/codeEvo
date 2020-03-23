import functools
import typing
import string
import random
import pytest

def leap(jz: int) -> bool:
    """ leap year wenn durch 4 teilbar, ODER durch 100 und 400 teilbar, wenn 100 aber nicht 400 normales jahr
        jz muss >= 1582 sein
       
    """
    if jz >= 1582:
        if jz // 4:
            print(jz, "ist ein Schaltjahr")
            return True
            print("ist ein Schaltjahr")
        elif jz // 100:
            if jz // 400:
                return True
                print("ist ein Schaltjahr")
            else:
                return False
                print("ist KEIN Schaltjahr")

print(leap(2004))
######################################################################
## Lösung Teil 2 (Tests)


######################################################################
