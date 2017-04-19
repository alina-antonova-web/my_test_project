from sct.tests.test_common import *


assert test_vocabulary(GOOD_FILE) == GOOD_ANSWER

another_good_file = MAIN_DIR + u'/text'
another_answer = "[('yxcvb', 5), ('asdf', 4), ('qwert', 4), ('test', 3), ('yxc', 3), ('asd', 2), ('qwe', 1)]"

assert test_vocabulary(another_good_file) == another_answer
