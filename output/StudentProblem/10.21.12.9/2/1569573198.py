============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:17: in <module>
    is_palindromic(1234)
/private/tmp/blabla.py:14: in is_palindromic
    n_str_reversed = reversed(n)
E   TypeError: 'int' object is not reversible
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: 'int' object is not reversible
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
