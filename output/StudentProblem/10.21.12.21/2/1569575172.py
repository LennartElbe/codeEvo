============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:15: in <module>
    print(is_palindromic(1001))
/private/tmp/blabla.py:11: in is_palindromic
    if s == inv(s):
E   NameError: name 'inv' is not defined
=========================== short test summary info ============================
ERROR ../../../../../tmp - NameError: name 'inv' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
