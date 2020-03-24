============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:65: in <module>
    print(word_count("/usr/share/doc/libpython3.6-minimal/copyright")) #(995,7030, 49852)
/private/tmp/blabla.py:53: in word_count
    with open('file') as f:
E   FileNotFoundError: [Errno 2] No such file or directory: 'file'
=========================== short test summary info ============================
ERROR ../../../../../tmp - FileNotFoundError: [Errno 2] No such file or direc...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
