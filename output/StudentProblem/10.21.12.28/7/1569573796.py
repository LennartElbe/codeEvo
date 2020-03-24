============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
        assert divisors(5) == [5]
>       assert divisors(6) == [3, 3]
E       assert [6, 6.0, 3.0] == [3, 3]
E         At index 0 diff: 6 != 3
E         Left contains one more item: 3.0
E         Use -v to get the full diff

/private/tmp/blabla.py:22: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert [6, 6.0, 3.0] == [3, 3]
============================== 1 failed in 0.06s ===============================
