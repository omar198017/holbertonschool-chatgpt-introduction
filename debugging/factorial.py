#!/usr/bin/python3
# Author: Omar Caguazango

import sys

if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)