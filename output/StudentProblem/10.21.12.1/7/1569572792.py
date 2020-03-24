============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test_5 ____________________________________

    def test_5():
>       assert divisors(10) == [1, 2, 5, 10]

/private/tmp/blabla.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 10

    def divisors(x: int):
        result = []
        for i in range(x + 1):
>           if not(x % i):
E           ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:11: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_5 - ZeroDivisionError: integer division or m...
============================== 1 failed in 0.05s ===============================
