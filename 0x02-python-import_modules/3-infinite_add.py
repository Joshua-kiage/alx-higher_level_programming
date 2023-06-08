#!/usr/bin/python3
# Exclude the script name from the arguments

import sys

args = sys.argv[1:]

result = 0
for arg in args:
    result += int(arg)

print(result)
