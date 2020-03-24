============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:32: in <module>
    assert Vigenere("ABCD").encrypt() == "1234"
E   TypeError: encrypt() missing 1 required positional argument: 'w'
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: encrypt() missing 1 required positional...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
