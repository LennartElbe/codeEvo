============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:28: in <module>
    assert fil(x1,l1)==[2,1,9]
E   NameError: name 'l1' is not defined
------------------------------- Captured stdout --------------------------------
None
=========================== short test summary info ============================
ERROR ../../../../../tmp - NameError: name 'l1' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
