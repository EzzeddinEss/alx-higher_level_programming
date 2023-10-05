#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    
    ac = len(args)

    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ac))
    for x in range(ac):
        print("{}: {}".format(x + 1, args[x]))
