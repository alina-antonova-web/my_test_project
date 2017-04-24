import shlex
import subprocess

from constants import *


def parse_text(text):
    try:
        output = text
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        output = e
    return output


def run_script(command_line):
    args = shlex.split(command_line)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    try:
        outs, errs = proc.communicate()
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        proc.kill()
        outs, errs = proc.communicate()

    output = proc.returncode
    output_text = outs.decode('utf-8')

    logging.info('Output_text: ' + output_text)
    if output_text:
        output = parse_text(output_text)

    return output


def run_reading_text_from_file(file_name):
    command_line = "python " + FILE_READING_SCRIPT_PATH + " " + file_name
    text = run_script(command_line)
    if type(text) != int:
        text = text.replace('\n', ' ')
        text = ' '.join(text.split())
    return text


# Test function for module
def _test():
    assert run_reading_text_from_file(BAD_FILE_FOR_TEST) == ERROR_CODE
    assert run_reading_text_from_file(GOOD_FILE_FOR_TEST) == GOOD_TEST_ANSWER, 'Result: ' + run_reading_text_from_file(GOOD_FILE_FOR_TEST) + '  ==  ' + str(GOOD_TEST_ANSWER)

if __name__ == '__main__':
    _test()
