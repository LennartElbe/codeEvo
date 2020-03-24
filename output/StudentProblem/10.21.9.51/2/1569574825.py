============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:16: in <module>
    is_palindromic(5)
/private/tmp/blabla.py:12: in is_palindromic
    print(n.split())
E   AttributeError: 'int' object has no attribute 'split'
=========================== short test summary info ============================
ERROR ../../../../../tmp - AttributeError: 'int' object has no attribute 'split'
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
