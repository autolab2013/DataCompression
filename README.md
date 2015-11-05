# SisterDan

LZW Compress & Decompress

- MyCode:
    - For CMS & report
    - Only ```compressed``` and ```decompress.py``` are needed for submission
    - ```compress_mac.py``` and ```decompress_mac.py``` works on my Macbook Pro, but cannot compile on amdpool.ece
        - amdpool.ece python version too old, not using ```with open```
    - ```compress.py```:
        - [x] generate ```compressed```
    - ```compressed```:
        - ```-rw-r--r--  1 nathanlrf  staff   1.1M Nov  5 09:48 compressed```
    - ```decompress.py``` tested on amdpool.ece:
        - [x] ```/opt/alttools/bin/python decompress.py```
        - [x] ```diff out.txt austen.txt```
        - [x] time: 2.26 ```/usr/bin/time --format %U /opt/alttools/bin/python decompress.py```
        - [x] python bytecode size : ```-rw-rw-r-- 1 1.6K Nov  5 09:35 decompress.pyc```

- Reference:
    - Sample code

- Template:
    - Skeleton code from teacher
