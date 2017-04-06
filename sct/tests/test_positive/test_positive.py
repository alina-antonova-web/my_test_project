from sct.tests import test_common
from constance import *


if test_common.test_vocabulary(GOOD_FILE)[1] == GOOD_ANSWER:
    exit(0)
else:
    # TODO: Print an error code which is expected and which is received! --> ???
    exit(ERROR_CODE)

# TODO: Test ouput of the script --> ?????