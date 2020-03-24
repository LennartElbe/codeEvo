============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
        iter1 = ["Hello, World", "Hallo, Welt"]
        iter2 = ["     "]
        iter3 = ["     ", ",,,,,"]
        assert word_count_iter(iter1) == (2, 4, 23)
        assert word_count_iter(iter2) == (1, 0, 5)
>       assert word_counter_iter(iter3) == (2, 0, 10)
E       NameError: name 'word_counter_iter' is not defined

/private/tmp/blabla.py:57: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - NameError: name 'word_coun...
============================== 1 failed in 0.06s ===============================
