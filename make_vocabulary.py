# -*- encoding: utf-8 -*-

import sys
import logging

from constants import *
from count_words import *


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=LOG_FILE_NAME)


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


def make_vocabulary():
    file = take_file_name()
    text = read_file(file)
    vocabulary = count_words(text)
    return vocabulary

if __name__ == '__main__':
    try:
        make_vocabulary()
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        exit(ERROR_CODE)
