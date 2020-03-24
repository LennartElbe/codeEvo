============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
>       assert(word_count_iter(["Hallo hier du", "Zahltag"]) == (4))
E       AssertionError: assert 9 == 4
E        +  where 9 = word_count_iter(['Hallo hier du', 'Zahltag'])

/private/tmp/blabla.py:50: AssertionError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - AssertionError: assert 9 == 4
============================== 1 failed in 0.05s ===============================
