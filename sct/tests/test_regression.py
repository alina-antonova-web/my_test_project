from sct.tests.test_common import *


def run_regression(test_files):  # TODO: Split in run_tests and print_result
    answer = ' '
    count_good_tests = 0
    count_bad_tests = 0
    failed_tests = ''

    for test in test_files:
        print('Executing test: ' + test)
        if run_script('python ' + TESTS_DIR + test):
            failed_tests += 'Test with ' + test + ' FAILED\n'
            count_bad_tests += 1
            print("  FAILED")
        else:
            count_good_tests += 1

    if count_bad_tests == 0:
        answer = 'All ' + str(count_good_tests) + ' tests have PASSED'
    else:
        if count_good_tests:
            answer += str(count_good_tests) + ' tests PASSED.'
        answer += '\n\n' + str(count_bad_tests) + ' tests FAILED:\n' + failed_tests

    return answer

list_of_tests = ['test_positive/test_positive.py',
                 'test_negative/test_empty_file.py',
                 'test_negative/test_dir.py',
                 'test_negative/test_permission.py']

print(run_regression(list_of_tests))

