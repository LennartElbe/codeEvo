import functools
import typing
import string
import random
import pytest

def fil(x:int,ls)->list:
    result=[]
    for i in ls:
        if i<=x:
            result+=[i]
        else:
            return None
    return result
      
