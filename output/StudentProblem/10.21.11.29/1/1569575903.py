============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
>       assert(word_count_iter(["Hallo hier du", "Zahltag"]) == (2, 4, 20))
E       assert (0, 0, 0) == (2, 4, 20)
E         At index 0 diff: 0 != 2
E         Use -v to get the full diff

/private/tmp/blabla.py:56: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (0, 0, 0) == (2, 4,...
============================== 1 failed in 0.05s ===============================
