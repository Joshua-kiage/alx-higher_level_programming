#!/usr/bin/python3

import sys

args = sys.argv[1:]  # Exclude the script name from the arguments

num_args = len(args)

print(f"Number of argument(s): {num_args}")

if num_args == 0:
    print(".", end="\n")
else:
    arg_label = "argument" if num_args == 1 else "arguments"
    print(f"{arg_label}:", end="\n")

    for i in range(num_args):
        print(f"{i + 1}: {args[i]}")
