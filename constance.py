import os


ERROR_CODE = 1
FILE_OPEN_MODE = 'r'


MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_FILE_NAME = MAIN_DIR + u'/my_log.log'

MAIN_SCRIPT_PATH = MAIN_DIR + u'/make_vocabulary.py'
BAD_FILE = 'fileNotExist'
GOOD_FILE = MAIN_DIR + u'/sct/tests/test_positive/file1.txt'
TESTS_DIR = MAIN_DIR + u'/sct/tests/'

GOOD_ANSWER = {'test': 3, 'asd': 2}
