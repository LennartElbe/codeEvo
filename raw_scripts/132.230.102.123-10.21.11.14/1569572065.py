import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Function to return list of elements from xs, which are smaller than or equal to x
    
    Args:
        x: an integer
        xs: a list
    Returns:
        a list which contains every element out of xs, smaller than or equal to x
    """
    res = []
    for i in xs:
        if i <= x:
            res += [i]
    return res
######################################################################
## hidden code

def mk_coverage():
    covered = set()
    target = set(range(6))
    count = 0
    
    def coverage(func):
        nonlocal covered, target, count
    
        def wrapper(x, xs):
            nonlocal covered, count
            if xs == []:
                covered.add(0)
            if len (xs) == 1:
                covered.add(1)
            if len (xs) > 1:
                covered.add(2)
            if x in xs:
                covered.add(3)
            if len ([y for y in xs if y < x]):
                covered.add(4)
            if len ([y for y in xs if y > x]):
                covered.add(5)
            r = func (x, xs)
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
    list_filter = coverage(list_filter)
except:
    pass

# Lösung Teil 2. (Test)

def test_empty():
    assert list_filter(5, []) == []
    
def test_mixed():
    assert list_filter(5, [1, 5, 10]) == [1, 5]
    
######################################################################
## hidden tests

pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])

from inspect import getfullargspec

class TestNames:
    def test_list_filter (self):
        assert list_filter
        assert 'x' in getfullargspec(list_filter).args
        assert 'xs' in getfullargspec(list_filter).args

class TestGrades:
    def test_docstring_present(self):
        assert list_filter.__doc__ is not None

    def test_typing_present(self):
        assert list_filter.__hints__ == typing.get_type_hints(self.list_filter_oracle)

    def test_coverage(self):
        assert coverage("achieved") == coverage("required")

    def list_filter_oracle(self, x:int, xs:list)->list:
        return [ y for y in xs if y <= x ]
        
    def check_filter (self, x, xs):
        assert list_filter (x, xs) == self.list_filter_oracle (x, xs)

    def test_correctness(self):
        for i in range (100):
            l = random.randrange (6)
            xs = [ random.randrange (10) for z in range(l) ]
            x = random.randrange (10)
            self.check_filter (x, xs)

