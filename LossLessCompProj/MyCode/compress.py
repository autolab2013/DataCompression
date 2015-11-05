import struct

USHRT_MAX = 65535
input_file = 'austen.txt'
test_file = 'test.txt'
char_list = [
    ' ',
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
]


def build_dict(clist):
    mydict = dict()
    index = 0
    for c in clist:
        mydict[c] = index
        index += 1
    return mydict

# with open(test_file, 'r') as fin:
with open(input_file, 'r') as fin:
    my_dict = build_dict(char_list)
    fout = open('compressed', 'wb')
    c = fin.read(1)
    word = c
    code = -1
    extend = ''
    while True:
        c = fin.read(1)
        # print "prefix is : |" + prefix + '|'
        # flush my_dict if it is too large
        if len(my_dict) >= USHRT_MAX:
            # print "flush dict with size : " + str(len(my_dict))
            my_dict = build_dict(char_list)
            # print "dict size : " + str(len(my_dict))

        if not c:
            # print "end of file:"
            if word:
                if word not in my_dict:
                    # my_dict.append(prefix)
                    next_index = len(my_dict) + 1
                    my_dict[word] = next_index
                # if not word[:-1]:
                #     break
                # code = my_dict.index(prefix[:-1])
                code = my_dict[word]
                bytecode = struct.pack("<H", code)
                fout.write(bytecode)
            break
        else:
            extend = word + c
            # print "extend is : |" + extend + '|'
            if extend in my_dict:
                # print "extend found: " + str(my_dict.index(extend))
                word = extend
            else:
                # print "new word added : |" + extend + '|'
                next_index = len(my_dict) + 1
                my_dict[extend] = next_index
                code = my_dict[word]
                # if code > USHRT_MAX:
                #     print "seq is " + extend[:-1]
                #     print "dict size : " + str(len(my_dict))
                #     print "too large: " + str(code)
                # print "code of |" + extend[:-1] + "| is : " + str(code)
                bytecode = struct.pack("<H", code)
                fout.write(bytecode)
                word = c


