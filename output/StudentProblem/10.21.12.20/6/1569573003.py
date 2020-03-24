============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
>       assert list_filter(4, [1,2,3,4,5,6]) == [1,2,3,4]
E       assert None == [1, 2, 3, 4]
E        +  where None = list_filter(4, [1, 2, 3, 4, 5, 6])

/private/tmp/blabla.py:18: AssertionError
----------------------------- Captured stdout call -----------------------------
[[[[[], 1], 2], 3], 4]
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - assert None == [1, 2, 3, 4]
============================== 1 failed in 0.06s ===============================
