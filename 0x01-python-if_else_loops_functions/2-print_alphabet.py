#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for letter in range(97, 122):
    if letter == ord(e) or letter == ord(q):
        continue
    print('{}'.format(chr(letter)), end="")
