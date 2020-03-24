============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_leap ___________________________________

    def test_leap():
>       assert(leap(2019)) == False
E       NameError: name 'false' is not defined

/private/tmp/blabla.py:16: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_leap - NameError: name 'false' is not defined
============================== 1 failed in 0.05s ===============================
