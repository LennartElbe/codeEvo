import functools
import typing
import string
import random
import pytest

def leap(n : int) -> bool:
    """takes a year n > 1582 and returns depending on the year either "Schaltjahr" or 
    "kein Schaltjahr" or "False" in case the year is to small. """
    if n >= 1582:
        return "False"
    if n%4 == 0:
        if n%100 == 0 and not n%400 == 0:
            return "kein Schaltjahr"
        return "Schaltjahr"
    else:
        return "kein Schaltjahr"
        
        
######################################################################
## hidden code

def mk_coverage():
    covered = set()
    target = set(range(4))
    count = 0
    
    def coverage(func):
        nonlocal covered, target, count
    
        def wrapper(year):
            nonlocal covered, count
            if year % 4 != 0:
                covered.add(0)
            elif year % 100 != 0:
                covered.add(1)
            elif year % 400 != 0:
                covered.add(2)
            else:
                covered.add(3)
            r = func (year)
            count += 1
            return r
        if func == "achieved": return len(covered)
        if func == "required": return len(target)
        if func == "count" : return count
        functools.update_wrapper(wrapper, func)
        return wrapper
    return coverage

coverage = mk_coverage ()
try:
    leap = coverage(leap)
except:
    pass

## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2001) == "kein Schaltjahr" # kein Schaltjahr
    assert leap(2300) == "Schaltjahr" #Schaltjahr
    assert leap(1581) == "False" #less than 1582
    
######################################################################
## hidden tests

pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])
from inspect import getfullargspec
class TestNames:
    def test_leap (self):
        assert leap
        assert 'year' in getfullargspec(leap).args

class TestGrades:
    def test_docstring_present(self):
        assert leap.__doc__ is not None

    def test_typing_present(self):
        assert leap.__hints__ == typing.get_type_hints(self.leap_oracle)

    def test_coverage(self):
        assert coverage("achieved") == coverage("required")

    def leap_oracle(self, year :int) -> bool:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
        
    def check_leap (self, year):
        assert leap (year) == self.leap_oracle (year)

    def test_correctness(self):
        for i in range (100):
            year = random.randrange (1582,2500)
            self.check_leap (year)
        for i in range (100):
            year = random.randrange (1600,3000, 100)
            self.check_leap (year)

