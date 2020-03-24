============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:29: in <module>
    assert list_filter(2,[-1,25,30, 0]) == [0,-1]
E   assert [-1, 0] == [0, -1]
E    +  where [-1, 0] = <function list_filter at 0x1089fd3b0>(2, [-1, 25, 30, 0])
=========================== short test summary info ============================
ERROR ../../../../../tmp - assert [-1, 0] == [0, -1]
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
