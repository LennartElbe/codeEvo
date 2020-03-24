============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
______________________________ test_list_filter_a ______________________________

    def test_list_filter_a():
        a = 3
        b = [1, 2, 3, 4, 5]
>       assert list_filter(a, b) == [1, 2, 3]

/private/tmp/blabla.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 3, xs = [1, 2, 3, 4, 5]

    def list_filter(x: int, xs: list) -> list:
        ret_list = []
        for i in xs:
            if i <= x:
>               ret_list + list(i)
E               TypeError: 'int' object is not iterable

/private/tmp/blabla.py:12: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter_a - TypeError: 'int' object is n...
============================== 1 failed in 0.05s ===============================
