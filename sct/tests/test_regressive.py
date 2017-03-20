from sct.tests import test_common


answer = ' '
count_good_tests = 0
count_bad_tests = 0
main_path = '/usr/bin/python3.5 /home/alina/my_test_project/sct/tests/'
if test_common.run_script(main_path + 'test_positive/test_positive.py'):
    answer += 'Test with positive file does not work\n'
    count_bad_tests += 1
else:
    count_good_tests += 1
if test_common.run_script(main_path + 'test_negative/test_empty_file.py'):
    answer += 'Test with empty file does not work\n'
    count_bad_tests += 1
else:
    count_good_tests += 1
if test_common.run_script(main_path + 'test_negative/test_dir.py'):
    answer += 'Test with directory does not work\n'
    count_bad_tests += 1
else:
    count_good_tests += 1
if test_common.run_script(main_path + 'test_negative/test_permission.py'):
    answer += 'Test with permission denied does not work\n'
    count_bad_tests += 1
else:
    count_good_tests += 1

if answer == ' ':
    answer = 'All ' + str(count_good_tests) + ' tests was Ok'
else:
    if count_good_tests:
        answer += 'But ' + str(count_good_tests) + ' tests was good.'
    answer = str(count_bad_tests) + ' test was not good.\n' + answer

print(answer)
