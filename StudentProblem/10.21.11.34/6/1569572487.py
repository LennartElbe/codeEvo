import functools
import typing
import string
import random
import pytest

def list_filter(x:int,ls)->list:
    result=[]
    for i in ls:
        if i<x or i ==x:
            result+=[i]
        else:
            return None
    return result
print(fil(40,[2,1,55,9]))

      
