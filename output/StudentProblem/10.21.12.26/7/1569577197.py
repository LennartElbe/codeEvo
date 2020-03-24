============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 3 items

../../../../../tmp .F.                                                   [100%]

=================================== FAILURES ===================================
____________________________________ test_2 ____________________________________

    def test_2():
>       assert divisors(10) == [1,2,4,5,10]
E       assert [1, 2, 5, 10] == [1, 2, 4, 5, 10]
E         At index 2 diff: 5 != 4
E         Right contains one more item: 10
E         Use -v to get the full diff

/private/tmp/blabla.py:19: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_2 - assert [1, 2, 5, 10] == [1, 2, 4, 5, 10]
========================= 1 failed, 2 passed in 0.05s ==========================
