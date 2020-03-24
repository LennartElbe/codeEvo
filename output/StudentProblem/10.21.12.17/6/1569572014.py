============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
>       assert list_filter([3, 2, 4, 7], 4) == [3, 2, 4]

/private/tmp/blabla.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

xs = [3, 2, 4, 7], x = 4

    def list_filter(xs: list, x: int) -> list:
        res = []
        for number in xs:
            if number == x:
>               res += number
E               TypeError: 'int' object is not iterable

/private/tmp/blabla.py:12: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - TypeError: 'int' object is not...
============================== 1 failed in 0.07s ===============================
