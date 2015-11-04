import struct

fin = open('austen.txt', 'r')
fopen = open('compressed', 'wb')

data = fin.read()

while data != '':
    