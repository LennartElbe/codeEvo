============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_divisors_a ________________________________

    def test_divisors_a():
        zahl = 2
>       assert divisors(zahl) == [0, 1, 2]

/private/tmp/blabla.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 2

    def divisors(n) -> list:
        """
    
        """
        ret_list = []
        i = 0
        while (i <= n):
>           if (n % i) == 0:
E           ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:15: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors_a - ZeroDivisionError: integer divi...
============================== 1 failed in 0.05s ===============================
