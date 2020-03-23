import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def is_palindromic(n: int):
    if not n > 0:
        return False
    else:
        if n == int(map(n, revert=True):
            return True
        else:
            return False
######################################################################
## hidden code

def mk_coverage():
    covered = set()
    target = set(range(6))
    count = 0
    original = None
    
    def coverage(func):
        nonlocal covered, target, count, original
    
        def wrapper(n):
            nonlocal covered, count
            s = str (n)
            lens = len (s)
            if lens == 1:
                covered.add(0)
            if lens == 2:
                covered.add(1)
            if (lens > 2) and ( lenr % 2 == 0):
                covered.add(2)
            if lens > 2 and lenr % 2 == 1:
                covered.add(3)
            r = func (n)
            if r:
                covered.add (4)
            else:
                covered.add (5)
            count += 1
            return r
        if func == "achieved": return len(covered)
        if func == "required": return len(target)
        if func == "count" : return count
        if func == "original": return original
        original = func
        if func.__doc__:
            wrapper.__doc__ = func.__doc__
        wrapper.__hints__ = typing.get_type_hints (func)
        return wrapper
    return coverage

coverage = mk_coverage()
try:
    is_palindromic = coverage(is_palindromic)
except:
    pass

## Lösung Teil 2. (Tests)
print(is_palindromic(25))
def test_is_palindromic():
    assert(is_palindromic(0)) == False
    assert(is_palindromic(1)) == True
######################################################################
## hidden restores unadorned function

is_palindromic = coverage ("original")

## Lösung Teil 3.

## Lösung Teil 4.

######################################################################
## test code

pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])

from inspect import getfullargspec
class TestNames:
    def test_is_palindromic(self):
        assert is_palindromic
        assert 'n' in getfullargspec(is_palindromic).args

    def test_gen_palindromic(self):
        assert gen_palindromic
        assert 'n' in getfullargspec(gen_palindromic).args
        
    def test_represent(self):
        assert represent
        assert 'n' in getfullargspec(represent).args

class TestGrades:
    def test_docstring_present(self):
        assert is_palindromic.__doc__ is not None
        assert gen_palindromic.__doc__ is not None
        assert represent.__doc__ is not None

    def test_typing_present(self):
        assert is_palindromic.__hints__ == typing.get_type_hints(self.is_palindromic_oracle)
        assert typing.get_type_hints (gen_palindromic) == typing.get_type_hints (self.gen_palindromic_oracle)
        assert typing.get_type_hints (represent) == typing.get_type_hints (self.represent_oracle)

    def test_coverage(self):
        assert coverage("achieved") == coverage("required")

    def is_palindromic_oracle(self, n:int)->list:
        s = str(n)
        while len (s) > 1:
            if s[0] != s[-1]:
                return False
            s = s[1:-1]
        return True

    def gen_palindromic_oracle (self, n:int):
        return (j for j in range (n + 1, 0, -1) if self.is_palindromic_oracle (j))
        
    def represent_oracle (self, n:int) -> list:
        for n1 in self.gen_palindromic_oracle (n):
            if n1 == n:
                return [n1]
            for n2 in self.gen_palindromic_oracle (n - n1):
                if n2 == n - n1:
                    return [n1, n2]
                for n3 in self.gen_palindromic_oracle (n - n1 - n2):
                    if n3 == n - n1 - n2:
                        return [n1, n2, n3]
        # failed to find a representation
        return []

    def test_is_palindromic(self):
        ## fill in
        for i in range (100):
            self.check_divisors (i)
            n = random.randrange (10000)
            self.check_divisors (n)

    def test_gen_palindromic(self):
        ## fill in
        pass

    def test_represent (self):
        def check(n, r):
            for v in r:
                assert self.is_palindromic_oracle (v)
                assert n == sum (r)
        
        for n in range (1,100):
            r = represent (n)
            check (n, r)

        for i in range (100):
            n = random.randrange (10000)
            r = represent (n)
            check (n, r)


