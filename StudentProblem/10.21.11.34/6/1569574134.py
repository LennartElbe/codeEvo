import functools
import typing
import string
import random
import pytest

def list_filter(x:int,ls)->list:
    for i in ls:
        result=[]
        if i>x:
            return None
    else:
        result.append(i)
    return result


      
