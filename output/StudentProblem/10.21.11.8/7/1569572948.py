============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(20) == [1, 2, 4, 5, 10]

/private/tmp/blabla.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 20

    def divisors(n: int) -> list:
        """Returns a list of all divisors(without a rest) of a given number.
        Args:
            n: an integer
        Returns:
            res: a list of all the divisors.
        """
        res = []
        for x in range(n):
>           if n%x == 0:
E           ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:17: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - ZeroDivisionError: integer divisi...
============================== 1 failed in 0.05s ===============================
