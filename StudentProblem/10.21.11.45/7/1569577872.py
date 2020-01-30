import functools
import typing
import string
import random
import pytest

def divisors(n, d):
    result = []
    if n <= 0:
        return result
    else:
        for i in range(1,n):
            if i % d != 0:
                continue
            else:
                result.append(i)
                return rresult
            
                
