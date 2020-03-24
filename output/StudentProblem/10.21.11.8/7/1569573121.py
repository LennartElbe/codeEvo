============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert divisors(20) == [1, 2, 4, 5, 10]
E       assert [2, 4, 5, 10] == [1, 2, 4, 5, 10]
E         At index 0 diff: 2 != 1
E         Right contains one more item: 10
E         Use -v to get the full diff

/private/tmp/blabla.py:30: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert [2, 4, 5, 10] == [1, 2, 4,...
============================== 1 failed in 0.05s ===============================
