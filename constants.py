import os
import logging


SUCCESS_CODE = 0
ERROR_CODE = 1
FILE_OPEN_MODE = 'r'


MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_FILE_NAME = MAIN_DIR + u'/my_log.log'
MAIN_SCRIPT_PATH = MAIN_DIR + u'/make_vocabulary.py'

DIR_OF_FILE_OPERATIONS_TESTS = MAIN_DIR + u'/sct/tests/basic_file_operations/'

BAD_FILE_FOR_TEST = 'fileNotExist'
PERMISSION_DENIED_FILE_FOR_TEST = DIR_OF_FILE_OPERATIONS_TESTS + u'test_data/permission_denied_file.txt'

GOOD_FILE_FOR_TEST = DIR_OF_FILE_OPERATIONS_TESTS + u'test_data/file1.txt'
GOOD_TEST_ANSWER = "[('test', 3), ('asd', 2)]"

SECOND_GOOD_FILE_FOR_TEST = DIR_OF_FILE_OPERATIONS_TESTS + u'test_data/text'
SECOND_GOOD_TEST_ANSWER = "[('yxcvb', 5), ('asdf', 4), ('qwert', 4), ('test', 3), ('yxc', 3), ('asd', 2), ('qwe', 1)]"


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=LOG_FILE_NAME)
