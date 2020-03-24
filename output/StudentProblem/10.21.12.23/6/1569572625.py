============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
/private/tmp/blabla.py:8: in <module>
    def list_filter(int:x, list:[xs]):
E   NameError: name 'x' is not defined
=============================== warnings summary ===============================
/private/tmp/blabla.py:23
  /private/tmp/blabla.py:23: PytestAssertRewriteWarning: assertion is always true, perhaps remove parentheses?
    assert(3,[1,2,3,4,5])

-- Docs: https://docs.pytest.org/en/latest/warnings.html
=========================== short test summary info ============================
ERROR ../../../../../tmp - NameError: name 'x' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.09s ==========================
