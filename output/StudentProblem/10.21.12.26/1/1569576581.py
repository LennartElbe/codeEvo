============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert word_count_iter("hallo") == ("?",1,5)

/private/tmp/blabla.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

it = 'hallo'

    def word_count_iter (it):
        """counts the number of words in input string
        args: it: input string
        returns: tuple with the number of lines, words and symbols in it (in this order)"""
        zahl = nwords (it)
        nummer = 0
        for i in it:
            nummer += 1
>       return tuple ("?",zahl,nummer)
E       TypeError: tuple expected at most 1 arguments, got 3

/private/tmp/blabla.py:30: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - TypeError: tuple expected at most 1 argume...
============================== 1 failed in 0.06s ===============================
