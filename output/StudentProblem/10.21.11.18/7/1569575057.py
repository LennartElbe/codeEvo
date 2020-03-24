============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 1 item

../../../../../tmp E                                                     [100%]

==================================== ERRORS ====================================
_______________________ ERROR at setup of test_divisors ________________________
file /private/tmp/blabla.py, line 18
  def test_divisors(n: int, d: int):
E       fixture 'n' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/private/tmp/blabla.py:18
=========================== short test summary info ============================
ERROR ../../../../../tmp/::test_divisors
=============================== 1 error in 0.01s ===============================
