============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:54: in <module>
    print(ord("z")) % 122
E   TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'
------------------------------- Captured stdout --------------------------------
122
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: unsupported operand type(s) for %: 'Non...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
