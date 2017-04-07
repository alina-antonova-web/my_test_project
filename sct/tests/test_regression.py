from sct.tests.test_common import *


def make_tests(test_files):
    answer = ' '
    count_good_tests = 0
    count_bad_tests = 0

    for test in test_files:
        if run_script('python ' + TESTS_DIR + test):
            answer += 'Test with ' + test + ' does not work\n'
            count_bad_tests += 1
        else:
            count_good_tests += 1

    if answer == ' ':
        answer = 'All ' + str(count_good_tests) + ' tests was Ok'
    else:
        if count_good_tests:
            answer += 'But ' + str(count_good_tests) + ' tests was good.'
        answer = str(count_bad_tests) + ' test was not good.\n' + answer

    return answer

list_of_tests = ['test_positive/test_positive.py', 'test_negative/test_empty_file.py', 'test_negative/test_dir.py',
                 'test_negative/test_permission.py']
print(make_tests(list_of_tests))

