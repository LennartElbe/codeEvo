============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:18: in <module>
    is_palindromic(202)
/private/tmp/blabla.py:13: in is_palindromic
    invert += num[i]
E   IndexError: string index out of range
=========================== short test summary info ============================
ERROR ../../../../../tmp - IndexError: string index out of range
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
