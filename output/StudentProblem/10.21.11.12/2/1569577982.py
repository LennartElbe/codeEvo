============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:27: in <module>
    is_palindromic(123)
/private/tmp/blabla.py:20: in is_palindromic
    if str_n[x] == n_reverse[x]:
E   NameError: name 'x' is not defined
=========================== short test summary info ============================
ERROR ../../../../../tmp - NameError: name 'x' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
