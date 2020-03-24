============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:15: in <module>
    print(divisors(9))
/private/tmp/blabla.py:12: in divisors
    res = [x for x in range(n) if n % x == 0 ]
/private/tmp/blabla.py:12: in <listcomp>
    res = [x for x in range(n) if n % x == 0 ]
E   ZeroDivisionError: integer division or modulo by zero
=========================== short test summary info ============================
ERROR ../../../../../tmp - ZeroDivisionError: integer division or modulo by zero
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
