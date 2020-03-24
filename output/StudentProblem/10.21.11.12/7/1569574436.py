============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:21: in <module>
    print(divisors(2))
/private/tmp/blabla.py:15: in divisors
    divisors_list = divisors_list.append(x)
E   AttributeError: 'NoneType' object has no attribute 'append'
=========================== short test summary info ============================
ERROR ../../../../../tmp - AttributeError: 'NoneType' object has no attribute...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
