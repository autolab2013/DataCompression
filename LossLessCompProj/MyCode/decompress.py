import struct

# encoded as unsigned short, pack format is "<H" little ending unsigned short
USHRT_MAX = 65535
input_file = 'compressed'
output_file = 'out.txt'
# compute the word frequency of austen.txt, found only this chars are used
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


# build <code, word> decoding table from char list
def build_table(clist):
    mytable = dict()
    index = 0
    for c in clist:
        mytable[index] = c
        index += 1
    return mytable


with open(input_file, 'r') as fin:
    fout = open(output_file, 'w')
    my_table = build_table(char_list)
    c = fin.read(2)
    code = struct.unpack('<H', c)[0]
    word = my_table[code]
    fout.write(word)
    entry = ''

    while True:
        # read 2 bytes at a time
        c = fin.read(2)

        # if the code table size is too large, reset it to orginal
        if len(my_table) >= USHRT_MAX:
            my_table = build_table(char_list)
            # print "table size is : " + str(len(my_table))
            # print "resized size is : " + str(len(my_table))
        if not c:
            # end of file
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
