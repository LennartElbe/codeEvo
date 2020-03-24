============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:20: in <module>
    is_palindromic(123)
/private/tmp/blabla.py:16: in is_palindromic
    n_reverse.append(str_n[i])
E   AttributeError: 'str' object has no attribute 'append'
=========================== short test summary info ============================
ERROR ../../../../../tmp - AttributeError: 'str' object has no attribute 'app...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
