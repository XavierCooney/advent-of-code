#!/bin/sh

if [ $# -ne 1 ]; then
    echo "usage: $0 spec" >&2
    exit 1
fi
if ! [ -f "$1.hs" ]; then
    echo "missing haskell file" >&2
    exit 1
fi
if ! [ -f "$1.in" ]; then
    echo "missing input file" >&2
    exit 1
fi

runhaskell << HASKELL
`cat "$1.hs"`
main = do
    contents <- readFile "$1.in"
    print $ day1 contents
    print $ day2 contents
HASKELL