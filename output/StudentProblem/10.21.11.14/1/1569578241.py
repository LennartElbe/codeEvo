============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp FF                                                    [100%]

=================================== FAILURES ===================================
__________________________________ test_empty __________________________________

    def test_empty():
>       assert word_count_iter("") == [(lines, 0), (words, 0), (letters, 0)]
E       NameError: name 'lines' is not defined

/private/tmp/blabla.py:53: NameError
__________________________________ test_norm ___________________________________

    def test_norm():
>       assert word_count_iter("Ab cd ef \n gh ij") == [(lines, 2), (words, 5), (letters, 10)]
E       NameError: name 'lines' is not defined

/private/tmp/blabla.py:56: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_empty - NameError: name 'lines' is not defined
FAILED ../../../../../tmp/::test_norm - NameError: name 'lines' is not defined
============================== 2 failed in 0.06s ===============================
