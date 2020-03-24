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
>       assert list_filter(a, 20) == [0]

/private/tmp/blabla.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = [], xs = 20

    def list_filter(x, xs):
        """
        """
        result = []
>       for element in xs:
E       TypeError: 'int' object is not iterable

/private/tmp/blabla.py:12: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test1 - TypeError: 'int' object is not iterable
============================== 1 failed in 0.05s ===============================
