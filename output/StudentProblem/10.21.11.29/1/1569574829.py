============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
>       assert(nwords("Ha Ho H") == 2)
    
    
    
    ######################################################################
    ## Lsung Teil 3. (Tests)
        """assert(nwords("HALLOHALLOHALLO") == 1)
        assert(nwords(" ") == 0)

/private/tmp/blabla.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 'Ha Ho H'

    def nwords(s):
        L = list(s)
        H = []
        n = 0
        i = 0
        for i in L:
            if i != " ":
>               i += 1
E               TypeError: can only concatenate str (not "int") to str

/private/tmp/blabla.py:15: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - TypeError: can only concatenate str...
============================== 1 failed in 0.05s ===============================
