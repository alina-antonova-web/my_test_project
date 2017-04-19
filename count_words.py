import doctest


def sort_popular_list(words):   # TODO: Add UT + alphabet sorting of words, Add empty test case
    sort_dict_popular = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return sort_dict_popular


def count_words(text):  # TODO: Add empty test case
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
    >>>

    """

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
