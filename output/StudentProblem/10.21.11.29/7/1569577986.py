============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_divisors _________________________________

    def test_divisors():
>       assert(divisors(4) == [1,2])
E       assert [4, 2, 1] == [1, 2]
E         At index 0 diff: 4 != 1
E         Left contains one more item: 1
E         Use -v to get the full diff

/private/tmp/blabla.py:29: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_divisors - assert [4, 2, 1] == [1, 2]
============================== 1 failed in 0.05s ===============================
