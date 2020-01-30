import functools
import typing
import string
import random
import pytest

def filterelement(x:int,ls)->list:
    result=[]
    for i in ls:
        if i<=x:
            result.append(i)
        else:
            return None
    return result
      
