#!/usr/bin/python3
def uppercase(str):
    for index in str[:]:
        if ord(index) >= ord('a') and ord(index) <= ord('z'):
            index = chr(ord(index) - 32)
        print("{:s}".format(index), end='')
    print()
