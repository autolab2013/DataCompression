# Needed for struct.unpack

import struct

# Initialize our list of phrases

phrases = ('THE',  # position 0
           'AND',  # position 1
           'TO',  # position 2
           'WAS',  # position 3
           'YOU',  # position 4
           'THAT',  # position 5
           'OF',  # position 6
           'WITH',  # position 7
           'HAVE',  # position 8
           'HER',  # position 9
           'HAD',  # position 10
           'NOT',  # position 11
           'IN',  # position 12
           'SHE',  # position 13
           'A',  # position 14
           'B',  # position 15
           'C',  # position 16
           'D',  # position 17
           'E',  # position 18
           'F',  # position 19
           'G',  # position 20
           'H',  # position 21
           'I',  # position 22
           'J',  # position 23
           'K',  # position 24
           'L',  # position 25
           'M',  # position 26
           'N',  # position 27
           'O',  # position 28
           'P',  # position 29
           'Q',  # position 30
           'R',  # position 31
           'S',  # position 32
           'T',  # position 33
           'U',  # position 34
           'V',  # position 35
           'W',  # position 36
           'X',  # position 37
           'Y',  # position 38
           'Z',  # position 39
           '\n',  # position 40
           ' ',  # position 41
           '!',  # position 42
           '"',  # position 43
           '&',  # position 44
           '\'',  # position 45
           '(',  # position 46
           ')',  # position 47
           ',',  # position 48
           '-',  # position 49
           '.',  # position 50
           '0',  # position 51
           '1',  # position 52
           '2',  # position 53
           '3',  # position 54
           '4',  # position 55
           '5',  # position 56
           '6',  # position 57
           '7',  # position 58
           '8',  # position 59
           '9',  # position 60
           ':',  # position 61
           ';',  # position 62
           '?',  # position 63
           )

# Open the input and output files. 'rb' is needed on some platforms
# to indicate that 'compressed' is a binary file.

fin = open('compressed', 'rb')
fout = open('out.txt', 'w')

# Read in the entire compressed file

indata = fin.read()

while (indata != ''):

    # Python has an "unpack" function that will take a string and
    # interpret it as a given type. Here we ask it to interpret the
    # first 3 remaining bytes of the compressed file + a dummy byte
    # as an unsigned, little-endian, integer.

    fourphrases = struct.unpack("<I", indata[0:3] + '\0')[0]

    # delete three bytes from the beginning of the file since we
    # have already extracted them.

    indata = indata[3:]

    # We have 4 phrases, each using 6 bits, encoded across the
    # unsigned integer fourphrases.

    for i in range(0, 4):
        ind = (fourphrases >> 6 * i) & 63
        fout.write(phrases[ind])

# 'compressed' does not include the final newline so we output it here

fout.write('\n')

# Close input and output files

fin.close()
fout.close()
