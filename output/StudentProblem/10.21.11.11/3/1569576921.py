============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
../../../Library/Python/3.7/lib/python/site-packages/_pytest/python.py:513: in _importtestmodule
    mod = self.fspath.pyimport(ensuresyspath=importmode)
../../../Library/Python/3.7/lib/python/site-packages/py/_path/local.py:701: in pyimport
    __import__(modname)
<frozen importlib._bootstrap>:983: in _find_and_load
    ???
<frozen importlib._bootstrap>:967: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:677: in _load_unlocked
    ???
../../../Library/Python/3.7/lib/python/site-packages/_pytest/assertion/rewrite.py:143: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
../../../Library/Python/3.7/lib/python/site-packages/_pytest/assertion/rewrite.py:330: in _rewrite_test
    co = compile(tree, fn, "exec", dont_inherit=True)
E     File "/private/tmp/blabla.py", line 19
E       break
E       ^
E   SyntaxError: 'break' outside loop
=========================== short test summary info ============================
ERROR ../../../../../tmp
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
