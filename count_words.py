import doctest

from constants import *


def sort_popular_list(words):
    """
    The function of sorting words by quantity and alphabet

    >>> sort_popular_list("")
    ''
    >>> sort_popular_list({'one':1})
    [('one', 1)]
    >>> sort_popular_list({'one': 1, 'two': 2, 'three': 2, 'four': 4})
    [('four', 4), ('three', 2), ('two', 2), ('one', 1)]
    >>> sort_popular_list({'test': 3, 'text': 2})
    [('test', 3), ('text', 2)]
    >>> sort_popular_list({'qwe': 3, 'asd': 4, 'yxc': 2})
    [('asd', 4), ('qwe', 3), ('yxc', 2)]
    >>> sort_popular_list({'ccc': 4, 'bbb': 2, 'aaa': 2})
    [('ccc', 4), ('aaa', 2), ('bbb', 2)]
    >>> sort_popular_list({'yxcvb': 5, 'qwert': 4, 'asdf': 4, 'yxc': 3, 'test': 3, 'asd': 2, 'qwe': 1})
    [('yxcvb', 5), ('asdf', 4), ('qwert', 4), ('test', 3), ('yxc', 3), ('asd', 2), ('qwe', 1)]
    >>>

    """

    if not words:
        logging.error('Failed. Empty list of words in sort_popular_list(words)')
        return ''

    index_of_quantity = 1
    index_of_word = 0
    sort_dict_popular = sorted(words.items(), key=lambda word: (-word[index_of_quantity], word[index_of_word]))
    return sort_dict_popular


def count_words(text):
    """
    The function of counting how many times words occur in the text

    >>> count_words("one two two three three three four four four four")
    [('four', 4), ('three', 3), ('two', 2), ('one', 1)]
    >>> count_words("test test test text text")
    [('test', 3), ('text', 2)]
    >>> count_words("qwe qwe qwe asd asd asd asd yxc yxc")
    [('asd', 4), ('qwe', 3), ('yxc', 2)]
    >>> count_words("aaa aaa bbb bbb bbb bbb ccc")
    [('bbb', 4), ('aaa', 2), ('ccc', 1)]
    >>> count_words("")
    ''
    >>> count_words("one")
    [('one', 1)]
    >>>

    """

    if not text:
        logging.error('Failed. Empty text in count_words(text)')
        return ''
    lines = [line.rstrip('\n') for line in text.split('\n')]
    words = {}
    for line in lines:
        for word in line.split(' '):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    popular_words = sort_popular_list(words)
    return popular_words


if __name__ == '__main__':
    doctest.testmod()
