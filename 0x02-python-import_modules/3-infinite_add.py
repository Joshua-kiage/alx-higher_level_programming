#!/usr/bin/python3

import sys

def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print(n)
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
        print(add)

if __name__ == "__main__":
    add_arg(sys.argv)
