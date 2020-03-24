============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        ls1=[2,1,9,40,55]
        x1 =40
        ls2=[1,2,3,4,5]
        x2=6
>       assert list_filter(x1,ls1)==[2,1,9,40]
E       assert [40] == [2, 1, 9, 40]
E         At index 0 diff: 40 != 2
E         Right contains 3 more items, first extra item: 1
E         Use -v to get the full diff

/private/tmp/blabla.py:30: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - assert [40] == [2, 1, 9, 40]
============================== 1 failed in 0.05s ===============================
