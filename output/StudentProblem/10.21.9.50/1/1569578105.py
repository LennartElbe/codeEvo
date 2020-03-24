============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:14: in <module>
    print(nwords("ht th"))
/private/tmp/blabla.py:10: in nwords
    for x in s.whitespace(" "):
E   AttributeError: 'str' object has no attribute 'whitespace'
=========================== short test summary info ============================
ERROR ../../../../../tmp - AttributeError: 'str' object has no attribute 'whi...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
