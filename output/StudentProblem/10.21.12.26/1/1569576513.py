============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert word_count_iter('hallo') == ("?",1,5)

/private/tmp/blabla.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/private/tmp/blabla.py:26: in word_count_iter
    zahl = nwords (it)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 'hallo'

    def nwords(s: string):
        """counts the number of words in input string n
        args: s: string with words to be counted
        returns: anzahl: number of words in sting """
        temp = 0
        anzahl = 0
>       for i in string:
E       TypeError: 'module' object is not iterable

/private/tmp/blabla.py:14: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - TypeError: 'module' object is not iterable
============================== 1 failed in 0.06s ===============================
