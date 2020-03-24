============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert(divisors(4)) == 4
E       assert [4] == 4
E        +  where [4] = divisors(4)

/private/tmp/blabla.py:28: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert [4] == 4
============================== 1 failed in 0.06s ===============================
