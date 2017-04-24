from read_text_from_file import *
from count_expressions import *


def make_dictionary():
    text = read_text_from_file()
    vocabulary = count_words(text)
    only_words = get_only_words(vocabulary)
    vocabulary.append(count_expressions(text, only_words))

    return vocabulary

if __name__ == '__main__':
    try:
        print(make_dictionary())
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        exit(ERROR_CODE)
