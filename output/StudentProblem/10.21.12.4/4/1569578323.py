============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:33: in <module>
    assert Vigenere().encrypt("ABCD") == "1234"
E   TypeError: __init__() missing 1 required positional argument: 'schluesselwort'
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: __init__() missing 1 required positiona...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
