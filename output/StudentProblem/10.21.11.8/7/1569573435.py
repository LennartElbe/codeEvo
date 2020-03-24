============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
        assert divisors(20) == [1, 2, 4, 5, 10, 20]
        assert divisors(7) == [1, 7]
>       assert divisors(1) == [1]
E       assert 1 == [1]
E        +  where 1 = divisors(1)

/private/tmp/blabla.py:33: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert 1 == [1]
============================== 1 failed in 0.05s ===============================
