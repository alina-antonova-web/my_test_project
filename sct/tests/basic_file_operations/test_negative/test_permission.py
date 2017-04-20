from sct.tests.test_common import *


if test_vocabulary(PERMISSION_DENIED_FILE_FOR_TEST) == ERROR_CODE:
    exit(SUCCESS_CODE)
else:
    exit(ERROR_CODE)
