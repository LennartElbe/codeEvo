============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:28: in <module>
    is_palindromic(123)
/private/tmp/blabla.py:23: in is_palindromic
    return n + " ist kein Palindrom"
E   TypeError: unsupported operand type(s) for +: 'int' and 'str'
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: unsupported operand type(s) for +: 'int...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
