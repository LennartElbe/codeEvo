============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:23: in <module>
    assert divisors(4) == [4,2,1]
E   assert [1, 2, 4] == [4, 2, 1]
E    +  where [1, 2, 4] = <function divisors at 0x10cfc4ef0>(4)
=========================== short test summary info ============================
ERROR ../../../../../tmp - assert [1, 2, 4] == [4, 2, 1]
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
