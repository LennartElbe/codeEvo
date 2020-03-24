============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(1) == [1]

/private/tmp/blabla.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/private/tmp/blabla.py:9: in divisors
    return [x for x in range(n + 1) if n % x == 0]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <range_iterator object at 0x1109d1900>

>   return [x for x in range(n + 1) if n % x == 0]
E   ZeroDivisionError: integer division or modulo by zero

/private/tmp/blabla.py:9: ZeroDivisionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - ZeroDivisionError: integer divisi...
============================== 1 failed in 0.06s ===============================
