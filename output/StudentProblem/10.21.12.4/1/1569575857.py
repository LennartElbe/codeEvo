============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:45: in <module>
    assert word_count_iter("Hallo das ist ein test") == (1,5,22)
E   AssertionError: assert <generator object word_count_iter at 0x10dbe2350> == (1, 5, 22)
E    +  where <generator object word_count_iter at 0x10dbe2350> = <function word_count_iter at 0x10dbe5050>('Hallo das ist ein test')
=========================== short test summary info ============================
ERROR ../../../../../tmp - AssertionError: assert <generator object word_coun...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
