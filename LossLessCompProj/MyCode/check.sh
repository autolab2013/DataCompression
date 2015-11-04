#!/bin/bash
if [ -e "austen.txt" ]; then
    echo "found austen.txt, original gzip compression is 964K"
    # ls -lh
    echo "start compress with compress.py..."
    # TODO: change to compress.py
    python compress.py
    echo "compress result:"
    ls -lh | grep 'compressed'
    echo "get decompress.py byte code size:"
    if [ -e "toBytecode.py" ] && [ -e "decompress.py" ]; then
        python toBytecode.py
        ls -lh | grep 'decompress.pyc'
        echo "start decompressing..."
        # TODO: change decompress.py
        # python decompress.py
        echo "compare decompressed result:"
        # diff out.txt austen.txt
    else
        echo "missing toBytecode.py or decompress.py, abort decompressing"
    fi
else
    echo "check if austen.txt exists!"
fi
