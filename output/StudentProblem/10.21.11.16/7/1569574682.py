============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:18: in <module>
    print(divisors(20))
/private/tmp/blabla.py:11: in divisors
    list.append(i)
E   TypeError: descriptor 'append' requires a 'list' object but received a 'int'
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: descriptor 'append' requires a 'list' o...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.09s ===============================
