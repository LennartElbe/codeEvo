============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:38: in <module>
    print(word_count_iter(["dg   ja n", "dg   ja n  "]))
/private/tmp/blabla.py:32: in word_count_iter
    for z in it():
E   TypeError: 'list' object is not callable
------------------------------- Captured stdout --------------------------------
0
0
1
2
3
3
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: 'list' object is not callable
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
