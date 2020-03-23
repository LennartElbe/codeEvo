import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str):
    """berechnet anz worte im string"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÜÖabcdefghijklmnopqrstuvwxyzüäö"
    take = 0
    skip = 0
    for i in s:
        if i not in letters:
            skip += 1
            #print("S:", skip)
        else:
            take += 1
            #print("t:", take)
    res = (len(s) - take) + 1
    return res

# manual testing:
if __name__ == '__main__':
    print(nwords("Hello world"))  # Anzahl der Woerter ist 2
    print(nwords("Dieser string hat fünf Wörter"))  
## Lösung Teil 2.
def word_count_iter():
    pass
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
    pass
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(filename):
    """ Schreiben Sie eine Funktion word_count, die einen Dateinamen f als Argument nimmt, 
        und als Ergebnis ein Tupel aus der:
        
        Anzahl der Zeilen, 
        der Anzahl der Worte
        Anzahl der Zeichen liefert,
        die aus der zugehörigen Datei gelesen worden sind.
        
        Beispiel: word_count("/usr/share/doc/libpython3.6-minimal/copyright") == (995, 7030, 49852)
    
    """
    with open(filename) as f:
        count_lines = 0
        anz_zeichen = 0
        f.read()
        nwords(filename)
        for line in f:
            count_lines += 1
        for i in f.read():
            anz_zeichen += 1
                
        return(nwords(filename), count_lines, anz_zeichen)

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


