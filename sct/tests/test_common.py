import shlex
import subprocess
from subprocess import PIPE


from constance import *


def run_script(command_line):
    args = shlex.split(command_line)
    out = subprocess.run(args, stdout=PIPE)
    output_text = out.stdout.decode('utf-8').replace('\n', '')
    if output_text:
        output_text = eval(output_text)
    return out.returncode, output_text


def test_vocabulary(file_name):
    command_line = "python " + MAIN_SCRIPT_PATH + " " + file_name
    return run_script(command_line)


# Test function for module
def _test():
    assert test_vocabulary(BAD_FILE)[0] == ERROR_CODE
    assert test_vocabulary(GOOD_FILE)[1] == GOOD_ANSWER

if __name__ == '__main__':
    _test()
