============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:13: in <module>
    print(is_palindromic(1001))
/private/tmp/blabla.py:11: in is_palindromic
    return s[0:,-1]
E   TypeError: string indices must be integers
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: string indices must be integers
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
