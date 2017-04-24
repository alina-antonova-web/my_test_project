from sct.tests.test_common import *


assert run_reading_text_from_file(GOOD_FILE_FOR_TEST) == GOOD_TEST_ANSWER
assert run_reading_text_from_file(SECOND_GOOD_FILE_FOR_TEST) == SECOND_GOOD_TEST_ANSWER
