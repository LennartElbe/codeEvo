============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:23: in <module>
    assert divisors(4) == [4,2,1]
/private/tmp/blabla.py:18: in divisors
    if n % teiler == 0:
E   ZeroDivisionError: integer division or modulo by zero
=========================== short test summary info ============================
ERROR ../../../../../tmp - ZeroDivisionError: integer division or modulo by zero
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
