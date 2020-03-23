import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def fil(x:int,ls)->list:
    result=[]
    for i in ls:
        if i<x or i ==x:
            result+=[i]
        else:
            return None
    return result
      
######################################################################
# Lösung Teil 2. (Test)

ls1 = [2,70,88,23,12,1,0]
x1 = 70
ls2=[1,2,3,4,5]
x2 =6


assert fil(x1,ls1)==[2,70,23,12,1,0]
assert fil(x2,ls2)==None
######################################################################
