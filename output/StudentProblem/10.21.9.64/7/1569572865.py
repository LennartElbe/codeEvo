============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert(divisors(10)) == [2, 5, 10]

/private/tmp/blabla.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 10

    def divisors(n: int) -> list:
        result = []
        for i in range(n+1):
>           if n % i == 0:
E           ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:11: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - ZeroDivisionError: integer divisi...
============================== 1 failed in 0.06s ===============================
