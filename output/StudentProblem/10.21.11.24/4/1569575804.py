============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:15: in <module>
    c = Vigenere("")
/private/tmp/blabla.py:13: in __init__
    raise TypeError("Key darf nicht leer sein")
E   TypeError: Key darf nicht leer sein
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: Key darf nicht leer sein
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
