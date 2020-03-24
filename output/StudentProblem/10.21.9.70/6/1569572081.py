============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
____________________________________ test1 _____________________________________

    def test1():
        a = []
        b = [1,2,3,4,5,6,7]
        c = [0, 2]
        d = [0.2, 0.5, 4.3]
>       assert list_filter(a) == []
E       TypeError: list_filter() missing 1 required positional argument: 'xs'

/private/tmp/blabla.py:24: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test1 - TypeError: list_filter() missing 1 requir...
============================== 1 failed in 0.05s ===============================
