============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:18: in <module>
    print(nwords_helper("habba"))
/private/tmp/blabla.py:10: in nwords_helper
    while s[count] not in string.whitespace:
E   IndexError: string index out of range
------------------------------- Captured stdout --------------------------------
False
=========================== short test summary info ============================
ERROR ../../../../../tmp - IndexError: string index out of range
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
