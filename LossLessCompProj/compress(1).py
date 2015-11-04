# Needed for struct.pack

import struct

# Initialize our list of phrases

prefices_tuple = ('THE',  # position 0
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

prefices = list(enumerate(prefices_tuple));


# Function that returns the longest phrase, and its index, that is a
# prefix of the given string

def find_encoding(en, string):
    for k, w in en:
        if string.startswith(w):
            return w, k


# Open the input and output files. 'wb' is needed on some platforms
# to indicate that 'compressed' is a binary file.

fin = open('austen.txt', 'r')
fout = open('compressed', 'wb')

# Read in the entire text file

data = fin.read();

# Initialize variables. We encode 4 sextuples of bits into four bytes,
# and 'sextuple' keeps track of which of the 4 we are currently on.
# encoding will store the 4 sextuples as an integer. outbytes is
# a bytearray that we use for writing to the 'compressed' file

sextuple = 0
encoding = 0
outbytes = bytearray(4)

while (data != ''):

    # Find the longest phrase that is a prefix and record the (phrase,index)
    # in (s,t). Then delete the phrase from the beginning of data.

    (s, t) = find_encoding(prefices, data)
    data = data[len(s):]

    # Store the phrase index in encoding, after rotating to the left by  
    # 6 bits

    encoding += t << (6 * sextuple)

    # If this the fourth sextuple, have Python convert the 'encoding'
    # integer into an array of 4 bytes, little-endian. Then write those
    # bytes to the output file and reset the sextuple counter and encoding
    # variable. Otherwise increment the sextuple counter # and keep going.

    if (sextuple < 3):
        sextuple += 1
    else:
        outbytes = struct.pack("<I", encoding)
        fout.write(outbytes[0:3])
        sextuple = 0
        encoding = 0

# Close the input and output files

fin.close()
fout.close()
