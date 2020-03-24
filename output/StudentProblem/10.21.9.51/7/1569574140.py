============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:26: in <module>
    print(divisors(4))
/private/tmp/blabla.py:23: in divisors
    return divisors(n)
/private/tmp/blabla.py:23: in divisors
    return divisors(n)
E   RecursionError: maximum recursion depth exceeded in comparison
!!! Recursion detected (same locals & position)
=========================== short test summary info ============================
ERROR ../../../../../tmp - RecursionError: maximum recursion depth exceeded i...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
