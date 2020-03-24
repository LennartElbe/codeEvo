============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
>       assert nwords("hello world") == 2

/private/tmp/blabla.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 'hello world'

    def nwords(s:string)-> int:
        """
            Args:
                s string
            return
                number of words
        """
>       t = random(1,2)
E       TypeError: 'module' object is not callable

/private/tmp/blabla.py:15: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - TypeError: 'module' object is not c...
============================== 1 failed in 0.05s ===============================
