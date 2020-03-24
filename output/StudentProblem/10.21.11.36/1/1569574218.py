============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:30: in <module>
    print(nwords("Hello, World!"))
/private/tmp/blabla.py:15: in nwords
    letters = string.ascii
E   AttributeError: module 'string' has no attribute 'ascii'
=========================== short test summary info ============================
ERROR ../../../../../tmp - AttributeError: module 'string' has no attribute '...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
