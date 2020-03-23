import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def is_palindromic(n: int) -> bool:
    """This function tests wether a positive integer s a palindrome or not
       A Palindrome is a Number where its the same read backwards
       Examples:
       is_palindromic(1001) == True
       is_palindromic(1000) == False
       """
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
######################################################################
## Lösung Teil 2. (Tests)
def test_8():
    assert is_palindromic(1001) == True
def test_9():
    assert is_palindromic(1000) == False
######################################################################
## Lösung Teil 3.
def gen_palindromic(n: int) -> list:
    """This function takes an integer n as input and
    returns every palindromic Number smaller or equal to 
    n
    
    Examples:
    gen_palindromic(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    gen_palindromic(11) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    
    """
    result = []
    for i in range(n + 1):
        if str(i) == str(i)[::-1]:
            result.append(i)
    return result
## Lösung Teil 4.
def represent(n: int) -> list:
    """This function takes a positiv integer and returns
       3 palindromic Numbers, which are equal to the poitiv 
       integer inserted if summed
    """
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


