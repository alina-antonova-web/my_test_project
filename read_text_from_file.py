# -*- encoding: utf-8 -*-
import sys

from count_words import *


def take_file_name():
    file_name = ''
    try:
        file_name = sys.argv[1]
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        exit(ERROR_CODE)
        raise
    return file_name


def read_file(file_name):
    # noinspection PyBroadException
    try:
        file = open(file_name, FILE_OPEN_MODE)
    except Exception as e:  # catch *all* exceptions
        logging.error('Failed.', exc_info=e)
        exit(ERROR_CODE)
    else:
        text = file.read()
        file.close()
    return text


def read_text_from_file():
    file = take_file_name()
    text = read_file(file)
    text = text.replace('\t', ' ')
    text = ' '.join(text.split('\n'))
    # vocabulary = count_words(text)
    # return vocabulary
    return text

if __name__ == '__main__':
    try:
        print(read_text_from_file())
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        exit(ERROR_CODE)
