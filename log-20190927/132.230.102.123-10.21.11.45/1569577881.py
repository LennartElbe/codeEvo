import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
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
            
                
######################################################################
## hidden code

def mk_coverage():
    covered = set()
    target = set(range(6))
    count = 0
    
    def coverage(func):
        nonlocal covered, target, count
    
        def wrapper(n):
            nonlocal covered, count
            if n <= 0:
                covered.add(0)
            if n == 1:
                covered.add(1)
            r = func (n)
            lenr = len (r)
            if lenr == 1:
                covered.add(2)
            if lenr == 2:
                covered.add(3)
            if (lenr > 2) and ( lenr % 2 == 0):
                covered.add(4)
            if lenr > 2 and lenr % 2 == 1:
                covered.add(5)
            count += 1
            return r
        if func == "achieved": return len(covered)
        if func == "required": return len(target)
        if func == "count" : return count
        if func.__doc__:
            wrapper.__doc__ = func.__doc__
        wrapper.__hints__ = typing.get_type_hints (func)
        return wrapper
    return coverage

coverage = mk_coverage()
try:
    divisors = coverage(divisors)
except:
    pass

## Lösung Teil 2. (Tests)
def test():
    assert divisors(4,2)
######################################################################
## hidden tests

pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])

from inspect import getfullargspec
class TestNames:
    def test_divisors (self):
        assert divisors
        assert 'n' in getfullargspec(divisors).args
        
class TestGrades:
    def test_docstring_present(self):
        assert divisors.__doc__ is not None

    def test_typing_present(self):
        assert divisors.__hints__ == typing.get_type_hints(self.divisors_oracle)

    def test_coverage(self):
        assert coverage("achieved") == coverage("required")

    def divisors_oracle(self, n:int)->list:
        return [ d for d in range (1, n + 1) if n % d == 0 ]
        
    def check_divisors (self, x):
        assert set(divisors (x)) == set(self.divisors_oracle (x))

    def test_correctness(self):
        for i in range (100):
            self.check_divisors (i)
            n = random.randrange (10000)
            self.check_divisors (n)

