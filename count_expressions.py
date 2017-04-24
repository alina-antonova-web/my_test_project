from count_words import *


def filter_by_occur(expressions):
    """
        Ignore expressions which happened only once

    >>> filter_by_occur("")
    ''
    >>> filter_by_occur([('qwe rtz', 3), ('vbn qwe', 2), ('rtz qwe', 1)])
    [('qwe rtz', 3), ('vbn qwe', 2)]
    >>> filter_by_occur([('qwe rtz', 3), ('yxc qwe', 2)])
    [('qwe rtz', 3), ('yxc qwe', 2)]
    >>>

    """
    def func(expression):
        if expression[1] > 1:
            return 1
        else:
            return 0
    if expressions:
        filtered_expressions = list(filter(func, expressions))
        return filtered_expressions
    else:
        return ''


def expressions_with_word(word, text):
    """
        Count expressions of 2 words with first word

    >>> expressions_with_word("","")
    ''
    >>> expressions_with_word("qwe", "qwe rtz asd yxc vbn qwe rtz 123 yxc vbn qwe rtz qwe")
    [('qwe rtz', 3), ('vbn qwe', 2)]
    >>> expressions_with_word("qwe", "qwe rtz asd yxc qwe rtz asd yxc qwe rtz asd yxc ")
    [('qwe rtz', 3), ('yxc qwe', 2)]
    >>> expressions_with_word("test", "test test test asd asd")
    [('test test', 2)]
    >>>

    """
    source = text.split()
    word_expressions = {}
    for i, w in enumerate(source):
        if w == word:
            if i+1 < len(source):
                second_word = source[i+1]
                expression = word + ' ' + second_word
                if expression in word_expressions:
                    word_expressions[expression] += 1
                else:
                    word_expressions[expression] = 1
            if i > 0:
                previous_word = source[i-1]
                if previous_word != word:
                    expression = previous_word + ' ' + word
                    if expression in word_expressions:
                        word_expressions[expression] += 1
                    else:
                        word_expressions[expression] = 1

    word_expressions = sort_list_by_popularity(word_expressions)
    word_expressions = filter_by_occur(word_expressions)

    return word_expressions


def count_expressions(text, words):
    """
    Count  expressions of 2 words only in addition to just words (ignore expressions and words which happened only once)

    >>> count_expressions("","")
    ''
    >>> count_expressions("", ['test', 'text'])
    ''
    >>> count_expressions("qwe rtz asd yxc vbn qwe rtz 123 yxc vbn qwe rtz qwe", ['qwe', 'rtz', 'vbn', 'yxc'])
    [('qwe rtz', 3), ('vbn qwe', 2), ('yxc vbn', 2)]
    >>> count_expressions("qwe rtz asd yxc qwe rtz asd yxc qwe rtz asd yxc ", ['asd', 'qwe', 'rtz', 'yxc'])
    [('asd yxc', 3), ('rtz asd', 3), ('qwe rtz', 3), ('yxc qwe', 2)]
    >>> count_expressions("test test test asd asd", ['test', 'asd'])
    [('test test', 2)]
    >>>

    """

    if not (text and words):
        logging.error('Failed. Empty text or words list in count_expressions')
        return ''

    text = ' '.join(text.split())
    all_expressions = []
    for word in words:
        word_expressions = expressions_with_word(word, text)
        for expression in word_expressions:
            if expression not in all_expressions:
                all_expressions.append(expression)

    return all_expressions


if __name__ == '__main__':
    doctest.testmod()
