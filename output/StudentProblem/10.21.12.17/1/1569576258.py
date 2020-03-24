============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:29: in <module>
    print(nwords(" "))
/private/tmp/blabla.py:19: in nwords
    nwords(s[1:])
/private/tmp/blabla.py:18: in nwords
    while s[0] in string.whitespace:
E   IndexError: string index out of range
------------------------------- Captured stdout --------------------------------
2
5
=========================== short test summary info ============================
ERROR ../../../../../tmp - IndexError: string index out of range
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
