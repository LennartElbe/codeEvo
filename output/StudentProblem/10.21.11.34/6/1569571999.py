============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:26: in <module>
    assert filterelement(x1,ls1)==[2,56,66,23,12,1,0]
E   NameError: name 'filterelement' is not defined
=========================== short test summary info ============================
ERROR ../../../../../tmp - NameError: name 'filterelement' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
