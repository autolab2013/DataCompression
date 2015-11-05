import struct

USHRT_MAX = 65535
input_file = 'compressed'
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


def build_table(clist):
    mytable = dict()
    index = 0
    for c in clist:
        mytable[index] = c
        index += 1
    return mytable


with open(input_file, 'r') as fin:
    fout = open('out.txt', 'w')
    my_table = build_table(char_list)
    c = fin.read(2)
    code = struct.unpack('<H', c)[0]
    word = my_table[code]
    fout.write(word)
    entry = ''

    while True:
        c = fin.read(2)
        if len(my_table) >= USHRT_MAX:
            # print "table size is : " + str(len(my_table))
            my_table = build_table(char_list)
            # print "resized size is : " + str(len(my_table))
        if not c:
            break
        else:
            code = struct.unpack('<H', c)[0]
            next_index = len(my_table) + 1
            if code in my_table:
                entry = my_table[code]
                my_table[next_index] = word + entry[0]
            else:
                entry = word + word[0]
                my_table[next_index] = entry
            fout.write(entry)
            word = entry

