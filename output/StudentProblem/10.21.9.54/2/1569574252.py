============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:23: in <module>
    assert is_palindromic(783) == False
E   assert None == False
E    +  where None = <function is_palindromic at 0x10684db90>(783)
=========================== short test summary info ============================
ERROR ../../../../../tmp - assert None == False
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
