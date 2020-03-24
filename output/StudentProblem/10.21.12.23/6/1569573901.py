============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test_3 ____________________________________

    def test_3():
>       assert list_filter(3,[0,1,2,3,4,5]) == [0,1,2]
E       assert None == [0, 1, 2]
E        +  where None = list_filter(3, [0, 1, 2, 3, 4, 5])

/private/tmp/blabla.py:29: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_3 - assert None == [0, 1, 2]
============================== 1 failed in 0.05s ===============================
