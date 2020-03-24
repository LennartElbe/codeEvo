============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp FF                                                    [100%]

=================================== FAILURES ===================================
_____________________________ test_word_count_iter _____________________________

    def test_word_count_iter():
>       assert word_count_iter(["foo bar", "baz"]) == (2, 3, 10)
E       assert (2, 2, 10) == (2, 3, 10)
E         At index 1 diff: 2 != 3
E         Use -v to get the full diff

/private/tmp/blabla.py:34: AssertionError
_______________________________ test_word_count ________________________________

    def test_word_count():
>       word_count("/usr/share/doc/libpython3.6-minimal/copyright") == (995,7030, 49852)

/private/tmp/blabla.py:47: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file = '/usr/share/doc/libpython3.6-minimal/copyright'

    def word_count(file) -> tuple:
>       with open(file) as fs:
E       FileNotFoundError: [Errno 2] No such file or directory: '/usr/share/doc/libpython3.6-minimal/copyright'

/private/tmp/blabla.py:43: FileNotFoundError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - assert (2, 2, 10) == (2, 3...
FAILED ../../../../../tmp/::test_word_count - FileNotFoundError: [Errno 2] No...
============================== 2 failed in 0.08s ===============================
