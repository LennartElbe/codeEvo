============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:47: in <module>
    assert word_count_iter("Hallo") == (1,1,5)
E   AssertionError: assert (0, 1, 5) == (1, 1, 5)
E    +  where (0, 1, 5) = <function word_count_iter at 0x10bc33dd0>('Hallo')
=========================== short test summary info ============================
ERROR ../../../../../tmp - AssertionError: assert (0, 1, 5) == (1, 1, 5)
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
