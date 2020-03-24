============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:20: in <module>
    is_palindromic(1)
/private/tmp/blabla.py:14: in is_palindromic
    if n == int(y[0]):
E   TypeError: int() argument must be a string, a bytes-like object or a number, not 'reversed'
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: int() argument must be a string, a byte...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
