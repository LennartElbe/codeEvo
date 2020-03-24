============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
        s = "Hey, what up"
>       assert(word_count_iter(s) == [1, 3])
E       assert [1, 0] == [1, 3]
E         At index 1 diff: 0 != 3
E         Use -v to get the full diff

/private/tmp/blabla.py:44: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert [1, 0] == [1, 3]
============================== 1 failed in 0.05s ===============================
