from sct.tests.test_common import *


if test_vocabulary('/home/alina/my_test_project/') == ERROR_CODE:
    exit(SUCCESS_CODE)
else:
    exit(ERROR_CODE)
