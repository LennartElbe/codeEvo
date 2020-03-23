import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
j = 1
k = 1.2
print(k < j)

def list_filter(x: int, xs: list) -> list:
    """ Funktion, die alle Elemente einer Liste
        ausgibt, die kleiner x sind.
        Args:
            x: ganze Zahl
            xs: Liste mit Zahlen
            
        Ergebnis:
            gefilterte Liste
    """
    xs_filt = []
    for i in xs:
#        if int(i) == i and i <= x:   # Abfangen von reellen, nicht-ganzen Zahlen
        if i <= x:
            print("i:", i, "xs_filt:", xs_filt)
            xs_filt.append(i)
        else:
            print("i:", i, "xs_filt:", xs_filt)
            xs_filt = xs_filt
    return xs_filt


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

def test_list_filter():
    xs1 = [1, 0, 2, 3, -1, -5]
    xs2 = [1, 5, 2, 3, 99, 2.5, 3.5]
    assert list_filter(0, xs1) == [0, -1, -5], "Fall x=0"
    assert list_filter(-2, xs1) == [-5], "Fall x=-2"
    assert list_filter(0, xs2) == [], "Fall: Bedingung fuer kein Element erfuellt"
    assert list_filter(3, xs2) == [1, 2, 3, 2.5], "Fall: reele Zahl groesser x enthalten"
    
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

