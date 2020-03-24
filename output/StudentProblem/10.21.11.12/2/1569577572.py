============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:26: in <module>
    is_palindromic(123)
/private/tmp/blabla.py:18: in is_palindromic
    for x in len(str_n):
E   TypeError: 'int' object is not iterable
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: 'int' object is not iterable
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
