============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(5) == [5]

/private/tmp/blabla.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 5.0

    def divisors(n :int) -> list:
        ls = []
        count = 1
>       while n % count == 0 and n != 0:
E       ZeroDivisionError: float modulo

/private/tmp/blabla.py:11: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - ZeroDivisionError: float modulo
============================== 1 failed in 0.05s ===============================
