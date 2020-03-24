============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:15: in <module>
    print(nwords("ht th"))
/private/tmp/blabla.py:11: in nwords
    for x in list(s).splice([" "]):
E   AttributeError: 'list' object has no attribute 'splice'
=========================== short test summary info ============================
ERROR ../../../../../tmp - AttributeError: 'list' object has no attribute 'sp...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
