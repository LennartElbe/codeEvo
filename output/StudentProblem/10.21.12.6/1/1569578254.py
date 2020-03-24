============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
        testlist1 = ["This is not a test."]
>       assert word_count_iter(testlist1) == (1, 5, 15)
E       TypeError: word_count_iter() takes 0 positional arguments but 1 was given

/private/tmp/blabla.py:31: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - TypeError: word_count_iter...
============================== 1 failed in 0.05s ===============================
