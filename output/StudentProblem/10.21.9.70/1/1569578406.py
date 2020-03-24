============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
        text1 = [["abc a b c"], [], ["a", "a"]]
        a = (n
             for lines in text1
             for n in lines
            )
>       assert word_count_iter(a) == (2, 6, 8)
E       assert (9, 9, 9) == (2, 6, 8)
E         At index 0 diff: 9 != 2
E         Use -v to get the full diff

/private/tmp/blabla.py:63: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (9, 9, 9) == (2, 6, 8)
============================== 1 failed in 0.05s ===============================
