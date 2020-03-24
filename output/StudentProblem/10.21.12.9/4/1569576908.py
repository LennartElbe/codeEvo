============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:63: in <module>
    print(test.encrypt("HELLO"))
/private/tmp/blabla.py:23: in encrypt
    keyword = self.key * (w_len // keylen) + 1
E   TypeError: can only concatenate str (not "int") to str
------------------------------- Captured stdout --------------------------------
ABC <class 'str'> 2 <class 'int'>
=========================== short test summary info ============================
ERROR ../../../../../tmp - TypeError: can only concatenate str (not "int") to...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
