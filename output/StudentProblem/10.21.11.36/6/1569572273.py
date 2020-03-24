============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_list_filter _______________________________

    def test_list_filter():
        #s1 = []
        ls1 = []
>       assert list_filter(0, ls1) == ls1

/private/tmp/blabla.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 0, xs = []

    def list_filter(x: int, xs: list):
        """Filter a given list with a given integer: Select all elements
        smaller as or equal to a given integer.
        Args:
            x (int): Filter integer
            xs (list): List to be filtered
        Returns:
            list: Containing all elements <= x
        """
>       if ls == []:
E       NameError: name 'ls' is not defined

/private/tmp/blabla.py:17: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_list_filter - NameError: name 'ls' is not de...
============================== 1 failed in 0.06s ===============================
