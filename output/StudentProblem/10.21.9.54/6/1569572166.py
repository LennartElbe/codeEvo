============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:16: in <module>
    assert list_filter(4,["hallo"]) == TypeError
/private/tmp/blabla.py:9: in list_filter
    return [a for a in xs if a <= x]
/private/tmp/blabla.py:9: in <listcomp>
    return [a for a in xs if a <= x]
E   TypeError: '<=' not supported between instances of 'str' and 'int'
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: '<=' not supported between instances of...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
