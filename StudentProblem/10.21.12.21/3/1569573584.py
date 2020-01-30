import functools
import typing
import string
import random
import pytest

def leap(jz: int):
    """ leap year wenn durch 4 teilbar, ODER durch 100 und 400 teilbar, wenn 100 aber nicht 400 normales jahr
        jz muss >= 1582 sein
 
    """
    if jz >= 1582:
        if jz % 4 == 0:
            #print(jz, "ist ein Schaltjahr")
            return True
        elif jz % 100 == 0:
            if jz % 400 == 0:
                #print(jz, "ist ein Schaltjahr")
                return True
            else:
                #print(jz, "ist KEIN Schaltjahr")
                return False
        else:
            #print(jz, "ist KEIN Schaltjahr")
            return False
    else:
        #print("Falsche Eingabe, keine Jahreszahl!")
        return False

if __name__ == '__main__':
    print(leap(2004))
    print(leap(2005))
    print(leap(1500))


