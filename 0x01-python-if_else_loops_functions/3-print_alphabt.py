#!/usr/bin/python3
for character in range(97, 123):
    if character not in [101, 113]:
        print(chr(character), end='')
