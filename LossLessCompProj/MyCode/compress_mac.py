import struct

# encoded as unsigned short, pack format is "<H" little ending unsigned short
USHRT_MAX = 65535
input_file = 'austen.txt'
output_file = 'compressed'
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


# build <word, code> encoding dictionary from char list
def build_dict(clist):
    mydict = dict()
    index = 0
    for c in clist:
        mydict[c] = index
        index += 1
    return mydict


with open(input_file, 'r') as fin:
    my_dict = build_dict(char_list)
    fout = open(output_file, 'wb')
    c = fin.read(1)
    word = c
    code = my_dict[word]
    entry = ''
    while True:
        c = fin.read(1)

        # flush my_dict if it is too large
        if len(my_dict) >= USHRT_MAX:
            my_dict = build_dict(char_list)
            # print "flush dict with size : " + str(len(my_dict))
            # print "dict size : " + str(len(my_dict))

        if not c:
            # end of file
            if word:
                if word not in my_dict:
                    next_index = len(my_dict) + 1
                    my_dict[word] = next_index
                code = my_dict[word]
                bytecode = struct.pack("<H", code)
                fout.write(bytecode)
            break
        else:
            entry = word + c
            # print "entry is : |" + entry + '|'
            if entry in my_dict:
                word = entry
            else:
                # add new entry to dictionary
                next_index = len(my_dict) + 1
                my_dict[entry] = next_index
                code = my_dict[word]
                # if code > USHRT_MAX:
                #     print "seq is " + entry[:-1]
                #     print "dict size : " + str(len(my_dict))
                #     print "too large: " + str(code)
                # print "code of |" + entry[:-1] + "| is : " + str(code)
                bytecode = struct.pack("<H", code)
                fout.write(bytecode)
                word = c


