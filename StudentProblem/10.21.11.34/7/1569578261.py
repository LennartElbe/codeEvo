import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def primelist(n)->list:
    """return a list of prime numbers"""
    ls=[]
    for i in range (2,n+1):
        for j in range(i+1,n+1):
            if i%j==0:
                break
        else:
            ls.append(i)
        return ls
         
def divisors(n:int)->list:
    res=[]
    if n in primelist(n):
        return [1,n]
    else:
        k=primelist(n)
    for i in k:
        if n%i==0:
            res+=[i]
        return res
        
            
        
        
######################################################################
## Lösung Teil 2. (Tests)

######################################################################
