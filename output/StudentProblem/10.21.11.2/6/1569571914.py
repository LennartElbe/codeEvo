============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_filter __________________________________

    def test_filter():
>       assert list_filter(2,[1,2,3]) == [2,3]

/private/tmp/blabla.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 2, xs = [1, 2, 3]

    def list_filter(x: int, xs: list) -> list:
        """ Function returns list of all elements from xs smaller than x.
        Args:   x: int,
                xs: list
    
        """
        l= []
        for i in xs: #looping
            if xs[i] >= i:
>               l  += xs[i]
E               TypeError: 'int' object is not iterable

/private/tmp/blabla.py:17: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_filter - TypeError: 'int' object is not iter...
============================== 1 failed in 0.06s ===============================
