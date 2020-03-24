============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
>       assert list_filter(4, [1,2,3,4,5,6]) == [1,2,3,4]

/private/tmp/blabla.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 4, xs = [1, 2, 3, 4, 5, 6]

    def list_filter(x: int, xs: list):
        same_or_smaller = []
>       for [i] in xs:
E       TypeError: cannot unpack non-iterable int object

/private/tmp/blabla.py:10: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - TypeError: cannot unpack non-i...
============================== 1 failed in 0.06s ===============================
