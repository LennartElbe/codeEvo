============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
        test = ["h i", "k z u"]
>       assert word_count_iter(test) == (0, 0, 0)
E       assert (2, 5, 8) == (0, 0, 0)
E         At index 0 diff: 2 != 0
E         Use -v to get the full diff

/private/tmp/blabla.py:46: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (2, 5, 8) == (0, 0, 0)
============================== 1 failed in 0.06s ===============================
