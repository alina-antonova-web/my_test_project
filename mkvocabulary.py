def mk_dictionary(text):
    text = text.strip()
    dictionary = {}

    for word in text.split(' '):
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    return dictionary

if __name__ == '__main__':
    assert mk_dictionary('test text test text test') == {"test": 3, "text": 2}, "Test text wrong"
    assert mk_dictionary('one two three') == {"one": 1, "three": 1, "two": 1}, "One two three does not work"
