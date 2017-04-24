import doctest

from constants import *


def sort_list_by_popularity(words):
    """
    The function of sorting words by quantity and alphabet

    >>> sort_list_by_popularity("")
    ''
    >>> sort_list_by_popularity({'one':1})
    [('one', 1)]
    >>> sort_list_by_popularity({'one': 1, 'two': 2, 'three': 2, 'four': 4})
    [('four', 4), ('three', 2), ('two', 2), ('one', 1)]
    >>> sort_list_by_popularity({'test': 3, 'text': 2})
    [('test', 3), ('text', 2)]
    >>> sort_list_by_popularity({'qwe': 3, 'asd': 4, 'yxc': 2})
    [('asd', 4), ('qwe', 3), ('yxc', 2)]
    >>> sort_list_by_popularity({'ccc': 4, 'bbb': 2, 'aaa': 2})
    [('ccc', 4), ('aaa', 2), ('bbb', 2)]
    >>> sort_list_by_popularity({'yxcvb': 5, 'qwert': 4, 'asdf': 4, 'yxc': 3, 'test': 3, 'asd': 2, 'qwe': 1})
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
    >>> count_words("aaa aaa bbb bbb    bbb bbb ccc")
    [('bbb', 4), ('aaa', 2), ('ccc', 1)]
    >>> count_words("qwe rtz  asd yxc qwe  rtz asd yxc qwe rtz asd yxc ")
    [('asd', 3), ('qwe', 3), ('rtz', 3), ('yxc', 3)]
    >>> count_words("")
    ''
    >>> count_words("one")
    [('one', 1)]
    >>>

    """

    if not text:
        logging.error('Failed. Empty text in count_words(text)')
        return ''
    lines = [' '.join(line.split()) for line in text.split('\n')]
    words_with_count = {}
    for line in lines:
        for word in line.split(' '):
            if word in words_with_count:
                words_with_count[word] += 1
            else:
                words_with_count[word] = 1

    popular_words_with_count = sort_list_by_popularity(words_with_count)
    return popular_words_with_count


def get_only_words(words_with_count):
    """
        The function of counting how many times words occur in the text

    >>> get_only_words([('four', 4), ('three', 3), ('two', 2), ('one', 1)])
    ['four', 'three', 'two', 'one']
    >>> get_only_words([('test', 3), ('text', 2)])
    ['test', 'text']
    >>> get_only_words([('asd', 4), ('qwe', 3), ('yxc', 2)])
    ['asd', 'qwe', 'yxc']
    >>> get_only_words([('bbb', 4), ('aaa', 2), ('ccc', 1)])
    ['bbb', 'aaa', 'ccc']
    >>> get_only_words([('asd', 3), ('qwe', 3), ('rtz', 3), ('yxc', 3)])
    ['asd', 'qwe', 'rtz', 'yxc']
    >>> get_only_words("")
    ''
    >>> get_only_words([('one', 1)])
    ['one']
    >>>

    """

    if not words_with_count:
        logging.error('Failed. Empty text in count_words(text)')
        return ''
    only_words = []
    for word_info in words_with_count:
        only_words.append(word_info[0])

    return only_words


if __name__ == '__main__':
    doctest.testmod()
