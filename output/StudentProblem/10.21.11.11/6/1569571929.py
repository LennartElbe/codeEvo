============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        x = 0
        xs = []
        assert list_filter(x, xs) == []
>       assert list_filter(1, [0,1,2]) == [0,1]

/private/tmp/blabla.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 1, xs = [0, 1, 2]

    def list_filter(x: int, xs: list) -> list:
        res = []
        for n in xs:
            if n <= x:
>               res += n
E               TypeError: 'int' object is not iterable

/private/tmp/blabla.py:12: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - TypeError: 'int' object is not...
============================== 1 failed in 0.05s ===============================
