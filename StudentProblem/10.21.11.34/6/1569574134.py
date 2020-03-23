import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x:int,ls)->list:
    for i in ls:
        result=[]
        if i>x:
            return None
    else:
        result.append(i)
    return result


      
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    ls1=[2,1,9,40,55]
    x1 =40
    ls2=[1,2,3,4,5]
    x2=6 
    assert list_filter(x1,ls1)==[2,1,9,40]
    assert list_filter(x2,ls2)==None



######################################################################
