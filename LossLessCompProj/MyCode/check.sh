#!/bin/bash
if [ -e "austen.txt" ]; then
    echo "search input files:"
    echo "  found austen.txt"
    echo "  original gzip compression is 964K"
    # ls -lh
    echo "start compress with compress.py..."
    echo ""
    # TODO: change to compress.py
    python compress.py
    echo "  compress result:"
    echo ""
    ls -lh | grep 'compressed'
    echo ""
    echo "get decompress.py byte code size:"
    echo ""
    if [ -e "toBytecode.py" ] && [ -e "decompress.py" ]; then
        echo "  compute python bytecode size..."
        echo ""
        python toBytecode.py
        ls -lh | grep 'decompress.pyc'
        echo ""
        echo "start decompressing..."
        # TODO: change decompress.py
        echo ""
        python decompress.py
        echo "compare decompressed result:"
        echo ""
        echo "diff result: "
        echo "  decompressed    ||      original"
        echo "      out.txt     ||      austen.txt"
        echo "  ===================================="
        if [[ $(diff out.txt austen.txt) ]]; then
            echo "      Error in decompressed result!"
            echo "      ============================="
            diff out.txt austen.txt
        else
            echo "        Match exactly!"
        fi
    else
        echo "missing toBytecode.py or decompress.py, abort decompressing"
    fi
else
    echo "check if austen.txt exists!"
fi
