============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:40: in <module>
    print(test_represent(100))
/private/tmp/blabla.py:37: in test_represent
    ss=s[0]+s[1]+s[2]
E   TypeError: 'NoneType' object is not subscriptable
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: 'NoneType' object is not subscriptable
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
