# Needed for struct.unpack

import struct

# Initialize our list of phrases

phrases = (
        'A', # position 0
        'B', # position 1
        'C', # position 2
        'D', # position 3
        'E', # position 4
        'F', # position 5
        'G', # position 6
        'H', # position 7
        'I', # position 8
        'J', # position 9
        'K', # position 10
        'L', # position 11
        'M', # position 12
        'N', # position 13
        'O', # position 14
        'P', # position 15
        'Q', # position 16
        'R', # position 17
        'S', # position 18
        'T', # position 19
        'U', # position 20
        'V', # position 21
        'W', # position 22
        'X', # position 23
        'Y', # position 24
        'Z', # position 25
       '\n', # position 26
        ' ', # position 27
        '!', # position 28
        '"', # position 29
        '&', # position 30
        '\'', # position 31
        '(', # position 32
        ')', # position 33
        ',', # position 34
        '-', # position 35
        '.', # position 36
        '0', # position 37
        '1', # position 38
        '2', # position 39
        '3', # position 40
        '4', # position 41
        '5', # position 42
        '6', # position 43
        '7', # position 44
        '8', # position 45
        '9', # position 46
        ':', # position 47
        ';', # position 48
        '?', # position 49
)

# Open the input and output files. 'rb' is needed on some platforms
# to indicate that 'compressed' is a binary file.

fin = open('compressed','rb')
fout = open('out.txt','w')

# Read in the entire compressed file

data = fin.read();
index_to_sym = dict(enumerate(phrases))

length = len(data)
count = len(index_to_sym)
dict_size = 65535
i = 1

phrase = struct.unpack("<H", data[0:2])[0]
word = index_to_sym[phrase]
fout.write(word)

while i < length / 2:
    if count >= dict_size:
        index_to_sym = dict(enumerate(phrases))
        count = len(index_to_sym)

    index = struct.unpack("<H", data[i * 2 : (i + 1) * 2])[0]
    if index in index_to_sym:
        entry = index_to_sym[index];
    elif index == count:
        entry = word + word[0]
    else:
        raise ValueError('Bad compressed k: %s' % index)
    fout.write(entry)

    #Add to dictionary
    index_to_sym[count] = word + entry[0]
    count += 1
    word = entry
    i += 1

fin.close()
fout.close()
