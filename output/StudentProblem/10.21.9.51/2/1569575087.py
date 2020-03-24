============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:15: in <module>
    print(is_palindromic(25))
/private/tmp/blabla.py:12: in is_palindromic
    return n % len(n)
E   TypeError: object of type 'int' has no len()
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: object of type 'int' has no len()
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
