============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:28: in <module>
    assert leap(2019) == False
E   assert True == False
E    +  where True = <function leap at 0x103f90ef0>(2019)
=========================== short test summary info ============================
ERROR ../../../../../tmp - assert True == False
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
