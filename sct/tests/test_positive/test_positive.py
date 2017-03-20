from sct.tests import test_common


if test_common.test_vocabulary('/home/alina/my_test_project/sct/tests/test_positive/file1.txt') == 0:
    exit(0)
else:
    exit(1)
