============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
        n1, n2, n3 = 1, 13, 20
>       assert divisor(n1) == [1]
E       NameError: name 'divisor' is not defined

/private/tmp/blabla.py:28: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - NameError: name 'divisor' is not ...
============================== 1 failed in 0.05s ===============================
