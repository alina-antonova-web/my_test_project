import sys
import logging

from constance import *


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=LOG_FILE_NAME)


def take_file_name():
    file_name = ''
    try:
        file_name = sys.argv[1]
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        exit(ERROR_CODE)
    return file_name


def read_file(file_name):
    # noinspection PyBroadException
    try:
        file = open(file_name, FILE_OPEN_MODE)
    except Exception as e:  # catch *all* exceptions
        logging.error('Failed.', exc_info=e)
        exit(ERROR_CODE)
    else:
        text = file.readlines()
        file.close()
    return text


def find_words(text):
    words = {}
    for line in text:
        line = line.replace('\n', '')
        for word in line.split(' '):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


def make_vocabulary():
    file = take_file_name()
    text = read_file(file)
    vocabulary = find_words(text)
    print(vocabulary)
    return vocabulary

if __name__ == '__main__':
    assert make_vocabulary()
