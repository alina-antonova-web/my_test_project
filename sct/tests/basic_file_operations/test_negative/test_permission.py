from sct.tests.test_common import *


if run_reading_text_from_file(PERMISSION_DENIED_FILE_FOR_TEST) == ERROR_CODE:
    exit(SUCCESS_CODE)
else:
    exit(ERROR_CODE)
