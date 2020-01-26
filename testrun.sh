source  env/bin/activate
nosetests --with-flaky -v --tc-file config/Base/base.conf --tc-file config/Stage/stage.conf -a type='smoke' TestCase/testcase.py