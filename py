#!/bin/sh

if [ $# -ne 1 ]; then
    echo "usage: $0 spec" >&2
    exit 1
fi
if echo "$1" | grep py; then
    echo "no"
    exit 1
fi

if ! [ -f "$1.py" ]; then
    echo "missing python... creating"
cat > "$1.py" << PY
from framework import *

s = read_input()
PY
    code "$1.py"
fi
if ! [ -f "$1.in" ]; then
    echo "missing input file... creating"
    touch "$1.in"
    code "$1.in"
fi

echo "running..."
python3 -m `echo "$1" | sed 's/\//./'`