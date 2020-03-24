============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 3 items

../../../../../tmp ..F                                                   [100%]

=================================== FAILURES ===================================
____________________________________ test_7 ____________________________________

    def test_7():
>       assert divisors(3) == [1]
E       assert [1, 3] == [1]
E         Left contains one more item: 3
E         Use -v to get the full diff

/private/tmp/blabla.py:22: AssertionError
----------------------------- Captured stdout call -----------------------------
1
3
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_7 - assert [1, 3] == [1]
========================= 1 failed, 2 passed in 0.05s ==========================
