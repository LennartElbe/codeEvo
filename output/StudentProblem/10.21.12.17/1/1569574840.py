============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:17: in <module>
    print(nwords_helper("habba ba"))
/private/tmp/blabla.py:12: in nwords_helper
    if s in string.whiespace:
E   AttributeError: module 'string' has no attribute 'whiespace'
=========================== short test summary info ============================
ERROR ../../../../../tmp - AttributeError: module 'string' has no attribute '...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
