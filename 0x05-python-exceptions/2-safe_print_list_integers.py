#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    count = 0
    while idx < x:
        try:
            print("{:d}".format(my_list[idx]), end='')
            count = count + 1
        except (TypeError, ValueError):
            pass
        idx = idx + 1
    print()
    return count
