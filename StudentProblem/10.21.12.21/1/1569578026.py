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
                
        return(nwords(filename), count_lines, )

######################################################################
