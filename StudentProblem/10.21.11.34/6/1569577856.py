import functools
import typing
import string
import random
import pytest

def list_filter(x:int,ls)->list: 
    for i in ls:
        result=[]
        if i>x or i==x:
            result+=[i]
        return result
    else:
        return None
        
    


      
