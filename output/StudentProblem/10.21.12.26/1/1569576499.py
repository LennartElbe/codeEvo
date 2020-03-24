============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________________ test _____________________________________

    def test():
>       assert word_count_iter(hallo) == ("?",1,5)
E       NameError: name 'hallo' is not defined

/private/tmp/blabla.py:34: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test - NameError: name 'hallo' is not defined
============================== 1 failed in 0.06s ===============================
