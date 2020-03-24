============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
        assert divisors(1) == [1]
>       assert divisors(3) == [1, 3]

/private/tmp/blabla.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 3

    def divisors(n:int)-> list:
        res = []
        if n == 1:
            return [n]
        else:
            for d in range(n):
>               if n%d == 0:
E               ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:14: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - ZeroDivisionError: integer divisi...
============================== 1 failed in 0.05s ===============================
