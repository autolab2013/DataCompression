# Needed for struct.pack

import struct

# Open the input and output files. 'wb' is needed on some platforms
# to indicate that 'compressed' is a binary file.

fin = open('austen.txt','r')
fout = open('compressed','w')

# Read in the entire text file

data = fin.read();


prefices_tuple = (
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

# def find_encoding(dic, string):
#     en = dic.keys()
#     for w in en:
#         if string.startswith(w):
#             return w,dic[w]

# index_to_sym = dict(enumerate(prefices_tuple))
# sym_to_index ={v : k for k, v in index_to_sym.items()}

# dict_size = 256
# sixtuple = 0
# outbytes = bytearray(4)
# encoding = 0
# count = len(index_to_sym)

# while data != '':
#     if count >= 256:
#         sym_to_index ={v : k for k, v in index_to_sym.items()}
#         count = len(sym_to_index)

#     s, t = find_encoding(sym_to_index, data)
#     data = data[len(s):]

#     sym_to_index[s + data[0]] = count
#     count += 1

#     encoding += t << (6 * sixtuple)

#     if sixtuple < 3:
#         sixtuple += 1
#     else:
#         outbytes = struct.pack("<I", encoding)
#         sixtuple = 0
#         encoding = 0



index_to_sym = dict(enumerate(prefices_tuple))
sym_to_index ={v : k for k, v in index_to_sym.items()}

i = 0
count = len(sym_to_index)
encoding = 0
length = len(data)
outbytes = bytearray(2)
#dictionary size is 255, if lager then clear
dict_size = 65535

while i < length:
    #restart the dictionary if it exceeds the maximum size
    if count >= dict_size:
        sym_to_index ={v : k for k, v in index_to_sym.items()}
        count = len(sym_to_index)

    j = i + 1
    while j <= length:
        phrase = data[i:j]
        if j == length and phrase in sym_to_index:
            #just get the index of the last phrase and not put into dictionary

            encoding = sym_to_index[phrase]
            print("Symbol: " + phrase)
            print("encoding: " + str(encoding))
            print("")
            outbytes = struct.pack("<H", encoding)
            fout.write(outbytes)
            j += 1
        elif phrase in sym_to_index:
            #if phrase exist in dictionary, move on
            j += 1
        else:
            #put new phrase into dictionary
            print("i: " + str(i) + " j: " + str(j))
            print("phrase: " + phrase + " length of phrase: " + str(len(phrase)))
            sym_to_index[phrase] = count
            count += 1

            encoding = sym_to_index[phrase[:-1]]
            print("Symbol: " + "'" + phrase[:-1] + "'")
            print("encoding: " + str(encoding))
            print("")
            outbytes = struct.pack("<H", encoding)
            fout.write(outbytes)
            encoding = 0
            break
    i = j - 1

# Close the input and output files

fin.close()
fout.close()
