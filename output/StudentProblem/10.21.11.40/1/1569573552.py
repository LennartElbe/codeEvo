============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
        assert word_count_iter(["foo bar", "baz"]) == (2, 3, 10)
>       assert word_count_iter(["a  b     c", "booooo1", "aa bb c"]) == (3, 7, 24)
E       assert (3, 12, 24) == (3, 7, 24)
E         At index 1 diff: 12 != 7
E         Use -v to get the full diff

/private/tmp/blabla.py:36: AssertionError
----------------------------- Captured stdout call -----------------------------
2 3 10
3 12 24
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (3, 12, 24) == (3, ...
============================== 1 failed in 0.05s ===============================
