import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Count the number of words in a given string. Words are separated by at least one char in string.whitespace
    Args:
        s (str): A string whose words are counted
    Returns: 
        int: Number of words in the given string
    """
    n = 0
    words = []
    current_word = ""
    for ch in s:
        if ch not in string.whitespace:
            # if its not whitespace, its a letter
            current_word += ch
        else:
            # only append word if its actually a word
            # (not only whitespace characters before)
            if len(current_word) > 0:
                words.append(current_word)
                current_word = ""
    if len(current_word) > 0:
        words.append(current_word)
    return len(words)

## Lösung Teil 2.
def word_count_iter(it) -> tuple:
    """Takes an iterable that yields a str in every iteration and returns a tuple
    with the number of lines, words and characters
    Args:
        it (iterable)
    Returns: 
        tuple 
    """
    lines, words, chars = 0, 0, 0
    for i in it:
        lines += 1
        words += nwords(i)
        chars += len(i)
    return lines, words, chars
        
print(word_count_iter(["     ", ",,,,,"]))    
######################################################################
## hidden code

def mk_coverage():
    covered = set()
    target = set(range(6))
    count = 0
    original = None
    
    def coverage(func):
        nonlocal covered, target, count, original
    
        def wrapper(it):
            nonlocal covered, count
            lit = list (it)
            r = func (lit)
            count += 1
            if lit == []:
                covered.add(0)
            elif len (lit) == 1:
                covered.add(1)
            else:
                covered.add(2)
            if "" in lit:
                covered.add (3)
            if len (lit) > 1:
                if [line for line in lit if [x for x in line if x in string.whitespace]]:
                    covered.add (4)
                else:
                    covered.add (5)
            return r
        if func == "achieved": return len(covered)
        if func == "required": return len(target)
        if func == "count" : return count
        if func == "original": return original
        original = func
        functools.update_wrapper (wrapper, func)
        return wrapper
    return coverage

coverage = mk_coverage()
try:
    word_count_iter = coverage(word_count_iter)
except:
    pass

## Lösung Teil 3. (Tests)
def test_word_count_iter():
    iter1 = ["Hello, World", "Hallo, Welt"]
    iter2 = ["     "]
    iter3 = ["     ", ",,,,,"]
    assert word_count_iter(iter1) == (2, 4, 23)
    assert word_count_iter(iter2) == (1, 0, 5)
    assert word_count_iter(iter3) == (2, 0, 10)
    
    
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
## hidden test code
pytest.main (["-v", "--assert=plain", "-p", "no:cacheprovider"])

from inspect import getfullargspec
class TestNames:
    def test_nwords (self):
        assert nwords
        assert 's' in getfullargspec(nwords).args
    def test_word_count_iter(self):
        assert word_count_iter
        
    def test_word_count(self):
        assert word_count
        assert 'file' in getfullargspec(word_count).args

class TestGrades:
    def test_docstring_present(self):
        assert nwords.__doc__ is not None
        assert word_count_iter.__doc__ is not None
        assert word_count.__doc__ is not None
    
    def test_typing_present (self):
        assert nwords.__annotations__ == self.nwords_oracle.__annotations__
        assert word_count_iter.__annotations__ == self.word_count_iter_oracle.__annotations__
        assert word_count.__annotations__ == self.word_count_oracle.__annotations__

    def nwords_oracle (self, s:str) -> int:
        return len (s.split())

    def test_nwords(self):
        charset = string.printable
        for i in range (100):
            s = ''.join (random.choice (charset) for j in range (1000))
            assert nwords (s) == self.nwords_oracle (s)

    def word_count_iter_oracle(self, iter):
        lines = 0
        words = 0
        chars = 0
        for line in iter:
            lines += 1
            chars += len(line)
            r = line.split()
            words += len(r)
        return (lines, words, chars)

    def test_wci_empty (self):
        assert word_count_iter ([]) == (0,0,0)

    def test_wci_one (self):
        assert word_count_iter (["a"]) == (1, 1, 1)

    def test_wci_simple (self):
        for i in range (50):
            assert word_count_iter (i * ["a"]) == (i,i,i)

    def test_wci_scale (self):
        for i in range (20):
            assert word_count_iter (i * ["a bb"]) == (i, 2*i, 4*i)

    def test_word_count_iter(self):
        charset = string.printable
        for i in range (100):
            l = random.randrange (10)
            subject = [''.join (random.choice (charset) for j in range (1000)) for k in range(l)] 
            assert word_count_iter (subject) == self.word_count_iter_oracle (subject)

    def word_count_oracle(self,file:str):
        return self.word_count_iter_oracle (open (file))

    def test_some_known_files(self):
        count = 3
        try:
            assert word_count ("/usr/share/dict/words") == (235886, 235886, 2493109)
        except:
            count = count - 1
        try:
            assert word_count ("/usr/share/doc/libpython3.6-minimal/copyright") == (995, 7030, 49855)
        except:
            count = count - 1
        try:
            f = "/data/test_code.py"
            assert word_count (f) == self.word_count_oracle (f)
        except:
            count = count - 1
        assert count > 0


