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
print(fil(40,[2,1,55,9]))

      
######################################################################
# Lösung Teil 2. (Test)

ls1 = [2,1,55,9]
x1 = 40
ls2=[1,2,3,4,5]
x2 =6
def test_list_filter(self):
    assert list_filter(x1,ls1)==[2,1,9]



######################################################################
