import functools
import typing
import string
import random
import pytest

def nwords(s:str)->int:
    count=0
    n=len(s)
    for i in s:
        if i==' ':
            count+=1
    result=n-count
    return result
    
      
    

