#!/usr/bin/python3
# 3-print_alphabt.py

for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
