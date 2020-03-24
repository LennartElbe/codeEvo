============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
>       assert list_filter(5, [1,2,3,4,5,6])== [1,2,3,4,5]

/private/tmp/blabla.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 5, xs = [1, 2, 3, 4, 5, 6]

    def list_filter(x: int, xs: list) -> list:
        if xs is None:
            return None
        else:
            for a in xs:
                n = []
                if a <= x:
>                   n.aapend(a)
E                   AttributeError: 'list' object has no attribute 'aapend'

/private/tmp/blabla.py:15: AttributeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - AttributeError: 'list' object ...
============================== 1 failed in 0.05s ===============================
