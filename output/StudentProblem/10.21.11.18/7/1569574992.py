============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(10)
E       TypeError: divisors() missing 1 required positional argument: 'd'

/private/tmp/blabla.py:19: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - TypeError: divisors() missing 1 r...
============================== 1 failed in 0.05s ===============================
