============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:19: in <module>
    assert divisors(8) == [1,2,4]
E   assert [8, 8, 8, 8] == [1, 2, 4]
E    +  where [8, 8, 8, 8] = <function divisors at 0x106c9f0e0>(8)
=========================== short test summary info ============================
ERROR ../../../../../tmp - assert [8, 8, 8, 8] == [1, 2, 4]
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
