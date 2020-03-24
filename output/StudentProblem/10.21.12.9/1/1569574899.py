============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
        assert word_count_iter([""]) == (1, 0, 0) #Contains a empty line
>       assert word_count_iter(["Hello", "World", "is nice"]) == (3, 4, 15)
E       assert (3, 4, 16) == (3, 4, 15)
E         At index 2 diff: 16 != 15
E         Use -v to get the full diff

/private/tmp/blabla.py:42: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (3, 4, 16) == (3, 4...
============================== 1 failed in 0.05s ===============================
