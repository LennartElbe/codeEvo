============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp .F                                                    [100%]

=================================== FAILURES ===================================
__________________________________ test_mixed __________________________________

    def test_mixed():
>       assert list_filter(5, [1, 5, 10]) == [1, 5]

/private/tmp/blabla.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 5, xs = [1, 5, 10]

    def list_filter(x: int, xs: list) -> list:
        """Function to return list of elements from xs, which are smaller than or equal to x
    
        Args:
            x: an integer
            xs: a list
        Returns:
            a list which contains every element out of xs, smaller than or equal to x
        """
        res = []
        for i in xs:
            if i <= x:
>               res += i
E               TypeError: 'int' object is not iterable

/private/tmp/blabla.py:20: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_mixed - TypeError: 'int' object is not iterable
========================= 1 failed, 1 passed in 0.06s ==========================
