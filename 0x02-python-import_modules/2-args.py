#!/usr/bin/python3
# Prints the number of and the list of its arguments

import sys

args = sys.argv[1:]
num_args = len(args)

if num_args > 1:
    print(f"{num_args} arguments:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
elif num_args == 0:
    print("0 arguments.")
else:
    print(f"{num_args} argument:")
    print(f"{num_args}: {args[0]}")
