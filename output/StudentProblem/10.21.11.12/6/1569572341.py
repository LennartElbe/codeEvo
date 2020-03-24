============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
>       assert list_filter(5, [1,2,4,5,8,9])

/private/tmp/blabla.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 5, xs = [1, 2, 4, 5, 8, 9]

    def list_filter(x: int, xs: list) -> list:
        filtered_list = []
        i = 1
        while i < len(xs):
            if x <= xs[i]:
>               xs[i] += filtered_list
E               TypeError: unsupported operand type(s) for +=: 'int' and 'list'

/private/tmp/blabla.py:13: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - TypeError: unsupported operand...
============================== 1 failed in 0.06s ===============================
