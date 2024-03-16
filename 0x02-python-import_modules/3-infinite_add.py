#!/usr/bin/python3
from sys import argv
add = 0
if __name__ == "__main__":
    for i in range(1, len(argv)):
        add += int(argv[i])

    print(add)
