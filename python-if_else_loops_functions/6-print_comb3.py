#!/usr/bin/python3
for index in range(0, 8):
    for pp in range(index, 10):
        if index != pp:
            print("{:d}{:d}, ".format(index, pp), end='')
print("89")
