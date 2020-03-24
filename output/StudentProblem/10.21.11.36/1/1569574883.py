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
>       assert word_count_iter(iter3) == (2, 0, 10)
E       assert (2, 1, 10) == (2, 0, 10)
E         At index 1 diff: 1 != 0
E         Use -v to get the full diff

/private/tmp/blabla.py:57: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (2, 1, 10) == (2, 0...
============================== 1 failed in 0.06s ===============================
