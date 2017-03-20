import shlex
import subprocess


# Exported functions
def run_script(command_line):
    args = shlex.split(command_line)
    out = subprocess.run(args)
    return out.returncode


def test_vocabulary(file_name):
    command_line = "/usr/bin/python3.5 /home/alina/my_test_project/make_vocabulary.py " + file_name
    return run_script(command_line)


# Test function for module
def _test():
    assert test_vocabulary('fileNotExist') == 1

if __name__ == '__main__':
    _test()
