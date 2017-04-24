from sct.tests.test_common import *
from count_words import *


GOOD_TEST_WORDS = [('test', 3), ('asd', 2)]
SECOND_GOOD_TEST_WORDS = [('yxcvb', 5), ('asdf', 4), ('qwert', 4), ('test', 3), ('yxc', 3), ('asd', 2), ('qwe', 1)]

FILES_WORDS = [(GOOD_FILE_FOR_TEST, GOOD_TEST_WORDS),
               (SECOND_GOOD_FILE_FOR_TEST, SECOND_GOOD_TEST_WORDS)]


def test_words_counter():
    for file in FILES_WORDS:
        print('Executing test: ' + str(file[0]))
        text = run_reading_text_from_file(file[0])
        vocabulary = count_words(text)
        if vocabulary == file[1]:
            print('Test count words PASSED \n')
        else:
            print('Test count words FAILED \n' + str(vocabulary) + '\n' + str(file[1]))

    return ''


GOOD_TEST_VOCABULARY = [('test', 3), ('asd', 2), [('test test', 2)]]
SECOND_GOOD_TEST_VOCABULARY = [('yxcvb', 5), ('asdf', 4), ('qwert', 4), ('test', 3), ('yxc', 3), ('asd', 2), ('qwe', 1),
                           [('yxcvb yxcvb', 4), ('asdf asdf', 3), ('qwert qwert', 3), ('test test', 2), ('yxc yxc', 2)]]

FILES_VOCABULARY = [(GOOD_FILE_FOR_TEST, GOOD_TEST_VOCABULARY),
                    (SECOND_GOOD_FILE_FOR_TEST, SECOND_GOOD_TEST_VOCABULARY)]


def test_make_dictionary():
    print('\nMake vocabulary test:\n')
    for file in FILES_VOCABULARY:
        print('Executing test: ' + str(file[0]))
        command_line = "python " + MAIN_SCRIPT_PATH + " " + file[0]
        text = run_script(command_line)
        text = text.replace('\n', ' ')
        text = ' '.join(text.split())
        if str(text) == str(file[1]):
            print('PASSED')
        else:
            print('FAILED. #' + text + '#-#' + str(file[1]) + '#')
    return ''

if __name__ == '__main__':
    test_words_counter()
    test_make_dictionary()
