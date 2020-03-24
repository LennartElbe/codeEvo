============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:20: in <module>
    assert divisors(0) == "falsche Eingabe"
E   AssertionError: assert 'falsch Eingabe' == 'falsche Eingabe'
E    +  where 'falsch Eingabe' = <function divisors at 0x104b1c050>(0)
=========================== short test summary info ============================
ERROR ../../../../../tmp - AssertionError: assert 'falsch Eingabe' == 'falsch...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
