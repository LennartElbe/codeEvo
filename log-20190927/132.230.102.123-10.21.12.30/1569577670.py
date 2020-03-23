import functools
import typing
import string
import random
import pytest

J1 = 1600 # 1600/4=400, 1600/400=4, 1600/100=16 ==> True
J2 = 1604 # nur durch 4 teilbar ==> True
J3 = 1603 # nicht durch 4 teilbar ==> False
J4 = 1700 # durch 4 und 100 teilbar, nicht durch 400 teilbar ==> False
print("J1= 1600:", J1 % 4, J1 % 100, J1 % 400)
print("J2= 1604:", J2 % 4, J2 % 100, J2 % 400)
print("J3= 1603:", J3 % 4, J3 % 100, J3 % 400)
print("J4= 1700:", J4 % 4, J4 % 100, J4 % 400)

def leap(Jahreszahl: int) -> bool:
    """ Funktion, die berechnet, ob eine gegebene Jahreszahl ein Schaltjahr ist.
    
        Args:
            Jahreszahl: ganzzahlige Zahl > 1582
            
        Ergebnis:
            True, wenn Schaltjahr, sonst False
    """
    Schaltjahr = False
    if Jahreszahl % 4 != 0:
        Schaltjahr = False
    elif Jahreszahl % 4 == 0:
        if Jahreszahl % 100 == 0 and Jahreszahl % 400 == 0:
            Schaltjahr = True
        elif Jahreszahl % 4 == 0:
            Schaltjahr = True
        else:
            Schaltjahr = False          
    return Schaltjahr

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
    assert leap(1600) == True, "Fall: durch 4, 100 und 400 teilbar"
    assert leap(1604) == True, "Fall: nur durch 4 teilbar"
    assert leap(1603) == False, "Fall: nicht durch 4 teilbar"
    assert leap(1700) == False, "Fall: durch 4 und 100 teilbar, nicht durch 400 teilbar"
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

