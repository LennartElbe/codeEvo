============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
        n1, n2, n3 = 1, 13, 20
        assert divisors(n1) == [1]
        assert divisors(n2) == [13, 1]
>       assert divisors(n3) == [20, 1, 2, 4, 5]
E       assert [20, 1, 2, 4, 5, 10] == [20, 1, 2, 4, 5]
E         Left contains one more item: 10
E         Use -v to get the full diff

/private/tmp/blabla.py:30: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert [20, 1, 2, 4, 5, 10] == [2...
============================== 1 failed in 0.06s ===============================
