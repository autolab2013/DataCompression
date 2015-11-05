from collections import OrderedDict
import operator
with open('austen.txt', 'r') as fin:
    word_dict = dict()
    c = fin.read(1)
    while c:
        if c not in word_dict:
            word_dict[c] = 1
        else:
            word_dict[c] += 1
        c = fin.read(1)

    sorted_dict = OrderedDict(sorted(word_dict.items()))
    my_dict = [
        ' ',
        '\n',
        '!',
        '"',
        '&',
        '\'',
        '(',
        ')',
        ',',
        '-',
        '.',
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        ':',
        ';',
        '?',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
    ]
    for word in sorted_dict:
        if word not in my_dict:
            print "missing entry in my_dict: " + word

    freq = sorted(sorted_dict.items(), key=operator.itemgetter(1))
    # print sorted_dict
    print freq
    # print my_dict
    # print my_dict.index('A')
    for word in freq:
        print word
    # for word in sorted_dict:
    #     print word
