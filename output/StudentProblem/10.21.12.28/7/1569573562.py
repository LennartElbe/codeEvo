============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(5) == [5]
E       assert [] == [5]
E         Right contains one more item: 5
E         Use -v to get the full diff

/private/tmp/blabla.py:19: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert [] == [5]
============================== 1 failed in 0.06s ===============================
