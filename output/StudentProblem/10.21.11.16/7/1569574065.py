============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:17: in <module>
    print(divisors(20))
/private/tmp/blabla.py:10: in divisors
    for i, k in range(n+1):
E   TypeError: cannot unpack non-iterable int object
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: cannot unpack non-iterable int object
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.08s ===============================
