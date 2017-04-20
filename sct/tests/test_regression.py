from sct.tests.test_common import *


def print_result(count_good_tests, count_bad_tests, failed_tests):
    result = '\n'
    if count_bad_tests == 0:
        result = 'All ' + str(count_good_tests) + ' tests have PASSED'
    else:
        if count_good_tests:
            result += str(count_good_tests) + ' tests PASSED.'
        result += '\n\n' + str(count_bad_tests) + ' tests FAILED:\n' + failed_tests
    print(result)
    return result


def run_regression(test_files):
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

    result = print_result(count_good_tests, count_bad_tests, failed_tests)

    return result


if __name__ == '__main__':
    list_of_tests = ['test_positive/test_positive.py',
                     'test_negative/test_empty_file.py',
                     'test_negative/test_dir.py',
                     'test_negative/test_permission.py']

    run_regression(list_of_tests)
