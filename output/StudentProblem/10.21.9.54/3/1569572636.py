============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:16: in <module>
    leap(2012)
/private/tmp/blabla.py:14: in leap
    reurn("kein Schaltjahr")
E   NameError: name 'reurn' is not defined
=========================== short test summary info ============================
ERROR ../../../../../tmp - NameError: name 'reurn' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
