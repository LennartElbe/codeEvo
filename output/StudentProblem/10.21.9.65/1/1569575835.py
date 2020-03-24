============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:27: in <module>
    print(nwords("Mah moud"))
/private/tmp/blabla.py:16: in nwords
    if s[i] != ' ':
E   IndexError: string index out of range
------------------------------- Captured stdout --------------------------------
0
1
1
2
2
3
3
3
4
5
5
6
6
7
7
8
8
=========================== short test summary info ============================
ERROR ../../../../../tmp - IndexError: string index out of range
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
