============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
>       assert word_count_iter(["foo bar", "baz"]) == (2, 3, 10)
E       AssertionError: assert None == (2, 3, 10)
E        +  where None = word_count_iter(['foo bar', 'baz'])

/private/tmp/blabla.py:34: AssertionError
----------------------------- Captured stdout call -----------------------------
2 3 10
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - AssertionError: assert Non...
============================== 1 failed in 0.06s ===============================
