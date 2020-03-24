============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:18: in <module>
    print(is_palindromic(25))
/private/tmp/blabla.py:12: in is_palindromic
    if n == int(filter(n, revert=True)):
E   TypeError: filter() takes no keyword arguments
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: filter() takes no keyword arguments
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
