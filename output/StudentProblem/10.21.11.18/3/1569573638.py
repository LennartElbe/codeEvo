============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
collected 2 items

../../../../../tmp EE                                                    [100%]

==================================== ERRORS ====================================
_________________________ ERROR at setup of test_leap1 _________________________
file /private/tmp/blabla.py, line 22
  def test_leap1(year) -> int:
E       fixture 'year' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/private/tmp/blabla.py:22
_________________________ ERROR at setup of test_leap2 _________________________
file /private/tmp/blabla.py, line 25
  def test_leap2(year) -> int:
E       fixture 'year' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/private/tmp/blabla.py:25
=========================== short test summary info ============================
ERROR ../../../../../tmp/::test_leap1
ERROR ../../../../../tmp/::test_leap2
============================== 2 errors in 0.02s ===============================
