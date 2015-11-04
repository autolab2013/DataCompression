TODO:
1.  Compress file into compressed
2.  Decompress compressed into out.txt

TASK:
1.  run on amdpool:
    ```
    /opt/alttools/bin/python decompress.py
    ```
2.  compare with austen.txt:
    ```
    diff out.txt austen.txt
    ```
3.  not use more than 15 minutes of CPU time in user mode on the Linux cluster:
    ```
    /usr/bin/time --format %U /opt/alttools/bin/python decompress.py
    ```
4.  length : decompress.pyc + compressed
    ```
    import py_compile
    py_compile.compile('decompress.py')
    ```
5.  gzip result: 943K
