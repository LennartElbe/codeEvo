============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test_2 ____________________________________

    def test_2():
        assert mysum([]) == 0
>       assert mysum([1,2,3]) == 6
E       assert 1 == 6
E        +  where 1 = mysum([1, 2, 3])

/private/tmp/blabla.py:20: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_2 - assert 1 == 6
============================== 1 failed in 0.05s ===============================
