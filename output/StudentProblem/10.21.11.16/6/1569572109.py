============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:17: in <module>
    print(list_filter(4, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
/private/tmp/blabla.py:11: in list_filter
    return list(m)
E   TypeError: 'int' object is not iterable
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: 'int' object is not iterable
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================