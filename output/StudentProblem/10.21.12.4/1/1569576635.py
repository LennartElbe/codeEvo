============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:48: in <module>
    assert word_count_iter("Hallo world") == (1,2,11)
E   AssertionError: assert (2, 2, 11) == (1, 2, 11)
E    +  where (2, 2, 11) = <function word_count_iter at 0x10c756440>('Hallo world')
=========================== short test summary info ============================
ERROR ../../../../../tmp - AssertionError: assert (2, 2, 11) == (1, 2, 11)
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
