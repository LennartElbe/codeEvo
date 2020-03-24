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

/private/tmp/blabla.py:63: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iterable_file = <generator object test_word_count_iter.<locals>.<genexpr> at 0x1041dc650>

    def  word_count_iter(iterable_file):
        """
         Funktion word_count_iter, die ein iterierbares Argument nimmt,
         das bei jeder Iteration eine Zeile (einen String) liefert,
         und als Ergebnis ein Tupel aus der Anzahl der Zeilen, der
         Anzahl der Worte und der Anzahl der Zeichen liefert, die aus
         dem Argument gelesen worden sind.
    
         args:
            iterable: str, tuple, list, gen, iter (iterirbares Objekt)
    
         returns:
            n: iter (Iterator )
         """
        num_lines = 0
        num_chars = 0
        num_words = 0
>       for a in next(iterable):
E       NameError: name 'iterable' is not defined

/private/tmp/blabla.py:45: NameError
=========================== short test summary info ============================
FAILED ../../../../../tmp/::test_word_count_iter - NameError: name 'iterable'...
============================== 1 failed in 0.05s ===============================
