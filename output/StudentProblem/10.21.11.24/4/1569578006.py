============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:36: in <module>
    print(c.encrypt("HALLO"))
/private/tmp/blabla.py:25: in encrypt
    o = o + c
E   TypeError: can only concatenate str (not "int") to str
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: can only concatenate str (not "int") to...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
