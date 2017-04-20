from sct.tests.test_common import *


file_name = TESTS_DIR + '/test_negative/permission_denied_file.txt'

if test_vocabulary(file_name) == ERROR_CODE:
    exit(SUCCESS_CODE)
else:
    exit(ERROR_CODE)
