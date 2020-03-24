============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_________________________________ test_nwords __________________________________

    def test_nwords():
>       assert nwords("Mein Name ist Jan") == 4 #normal

/private/tmp/blabla.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 'Mein Name ist Jan'

    def nwords(s: str) -> int:
        """Counts the numbers of words and returns it of a given string s"""
        b = 0
        w = 0
        for i in range(len(s)): #take every single element of string s
>           if s[i] == True and not s[i] == " ": #if not space add element to b
E           NameError: name 'n' is not defined

/private/tmp/blabla.py:13: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_nwords - NameError: name 'n' is not defined
============================== 1 failed in 0.04s ===============================
