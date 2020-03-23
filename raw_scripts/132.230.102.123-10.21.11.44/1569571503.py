import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.

def mysum(zs:list) -> int:    
    return sum(xs)
## Lösung Teil 2. (Tests)
def test_2():    
    assert mysum([1,2,3]) == 6
######################################################################
## hidden tests
pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])
from inspect import getfullargspec
mysumargs = getfullargspec(mysum).args
class TestName:
    def test_mysum (self):
        assert mysum
        assert 'xs' in mysumargs

class TestGrades:
    def test_docstring_present(self):
        assert False

    def test_typing_present(self):
        assert True

    def test_coverage(self):
        assert False

    def sum_oracle(self, xs:list)->int:
        return sum(xs)
        
    def check_sum (self,xs):
        assert mysum (xs) == self.sum_oracle (xs)

    def test_correctness(self):
        for i in range (100):
            l = random.randrange (6)
            xs = [ random.randrange (10) for z in range(l) ]
            self.check_sum (xs)

