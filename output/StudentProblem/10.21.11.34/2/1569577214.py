============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:40: in <module>
    print(test_represent(100))
/private/tmp/blabla.py:36: in test_represent
    s=res.sort(key=1)
E   TypeError: 'int' object is not callable
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: 'int' object is not callable
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
