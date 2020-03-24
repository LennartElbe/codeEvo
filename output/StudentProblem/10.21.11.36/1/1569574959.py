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
        iter3 = ("Hello", "World")
>       assert word_count_iter(iter1) == (2, 4, 23)
E       assert (2, 2, 23) == (2, 4, 23)
E         At index 1 diff: 2 != 4
E         Use -v to get the full diff

/private/tmp/blabla.py:54: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (2, 2, 23) == (2, 4...
============================== 1 failed in 0.05s ===============================
