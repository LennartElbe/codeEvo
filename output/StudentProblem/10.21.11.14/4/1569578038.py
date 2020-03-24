============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp FF                                                    [100%]

=================================== FAILURES ===================================
___________________________________ test_enc ___________________________________

    def test_enc():
>       assert encrypt(Hello)
E       NameError: name 'encrypt' is not defined

/private/tmp/blabla.py:29: NameError
___________________________________ test_dec ___________________________________

    def test_dec():
>       assert decrypt()
E       NameError: name 'decrypt' is not defined

/private/tmp/blabla.py:32: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_enc - NameError: name 'encrypt' is not defined
FAILED ../../../../../tmp/::test_dec - NameError: name 'decrypt' is not defined
============================== 2 failed in 0.07s ===============================
