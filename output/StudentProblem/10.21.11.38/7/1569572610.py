============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(4) == [1,2,4]

/private/tmp/blabla.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 4

    def divisors(n: int) -> list:
        """this function checks whether d is a Teiler of n
        Args: n a positive natural number
        returns: a list of all the Teilers with no repetitions"""
        res = []
        for d in range(0,n + 1):
>           if n % d == 0:
E           ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:14: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - ZeroDivisionError: integer divisi...
============================== 1 failed in 0.06s ===============================
