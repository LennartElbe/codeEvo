============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_divisor _________________________________

    def test_divisor():
>       assert divisor(6) == ["1","2","3","6"]
E       NameError: name 'divisor' is not defined

/private/tmp/blabla.py:23: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisor - NameError: name 'divisor' is not d...
============================== 1 failed in 0.04s ===============================
