============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp .F                                                    [100%]

=================================== FAILURES ===================================
______________________________ test_list_filter_b ______________________________

    def test_list_filter_b():
        a = 3
        b = [1, 2, 3, 4, 5]
>       assert list_filter(a, b) == [2, 3]
E       assert [1, 2, 3] == [2, 3]
E         At index 0 diff: 1 != 2
E         Left contains one more item: 3
E         Use -v to get the full diff

/private/tmp/blabla.py:24: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter_b - assert [1, 2, 3] == [2, 3]
========================= 1 failed, 1 passed in 0.05s ==========================
