============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp F                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_w_c_iter _________________________________

    def test_w_c_iter():
>       assert word_count_iter("hello") == (1, 1, 5)

/private/tmp/blabla.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 'hello'

    def word_count_iter(n: iter) -> str:
        """
        An iterator that returns the number of rows, words and symbols in a given iterable object.
        n: An iterable object
        """
        if len(n) != 0:
            sym = len(n) + 1
            # count up one row, if row length is reached
            if len(n) > 72:
                rows += 1
            words = 0
>           for a in range(n + 1):
E           TypeError: can only concatenate str (not "int") to str

/private/tmp/blabla.py:31: TypeError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_w_c_iter - TypeError: can only concatenate s...
============================== 1 failed in 0.06s ===============================
