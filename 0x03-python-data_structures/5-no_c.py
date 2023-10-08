#!/usr/bin/python3

def no_c(my_string):
    rm_chr = ""
    for idx in range(len(my_string)):
        if (my_string[idx] != 'c' and my_string[idx] != 'C'):
            rm_chr = rm_chr + my_string[idx]
    return (rm_chr)
