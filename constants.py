import os
import logging

SUCCESS_CODE = 0
ERROR_CODE = 1
FILE_OPEN_MODE = 'r'

MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_FILE_NAME = MAIN_DIR + u'/my_log.log'
FILE_READING_SCRIPT_PATH = MAIN_DIR + u'/read_text_from_file.py'
MAIN_SCRIPT_PATH = MAIN_DIR + u'/make_dictionary.py'

DIR_OF_TESTS_FILES = MAIN_DIR + u'/sct/tests/'
DIR_OF_FILE_OPERATIONS_TESTS = MAIN_DIR + u'/sct/tests/basic_file_operations/'

BAD_FILE_FOR_TEST = 'fileNotExist'
PERMISSION_DENIED_FILE_FOR_TEST = DIR_OF_FILE_OPERATIONS_TESTS + u'test_data/permission_denied_file.txt'

GOOD_FILE_FOR_TEST = DIR_OF_FILE_OPERATIONS_TESTS + u'test_data/file1.txt'
GOOD_TEST_ANSWER = "test test test asd asd"

SECOND_GOOD_FILE_FOR_TEST = DIR_OF_FILE_OPERATIONS_TESTS + u'test_data/text'
SECOND_GOOD_TEST_ANSWER = "test test test qwe asd asd yxc yxc yxc qwert qwert qwert qwert asdf asdf asdf asdf yxcvb yxcvb yxcvb yxcvb yxcvb"

logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=LOG_FILE_NAME)
