============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:45: in <module>
    print(Node (Leaf(1), Leaf(2)).preorder())
E   NameError: name 'Leaf' is not defined
=========================== short test summary info ============================
ERROR ../../../../../tmp - NameError: name 'Leaf' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
