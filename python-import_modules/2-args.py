#!/usr/bin/python3
import sys
if __name__ == "__main__":
    cb = len(sys.argv)
    if cb == 1:
        print("0 arguments.")
    elif cb == 2:
        print("1 argument:\n1: {}".format(str(sys.argv[1])))
    else:
        print("{} arguments:".format(cb - 1))
        for i in range(len(sys.argv)):
            if i != 0:
                print("{}: {}".format(i, str(sys.argv[i])))
