#!/usr/bin/python3
def remove_char_at(str, z):
    new = ""
    b = 0
    for c in str:
        if b != z:
            new += c
        b += 1
    return new
