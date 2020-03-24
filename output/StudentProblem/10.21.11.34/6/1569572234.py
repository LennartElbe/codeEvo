============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:26: in <module>
    assert fil(x1,ls1)==[2,1,9]
E   assert None == [2, 1, 9]
E    +  where None = <function fil at 0x10c8e9170>(40, [2, 1, 55, 9])
=========================== short test summary info ============================
ERROR ../../../../../tmp - assert None == [2, 1, 9]
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
