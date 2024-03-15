#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i == 1:
        print('{:d} argument'.format(i), end=":\n" if (i) != 0 else ".\n")
    else:
        print('{:d} arguments'.format(i), end=":\n" if (i) != 0 else ".\n")
    if (i) != 0:
        for j in range(1, i + 1):
            print('{:d}: {:s}'.format(j, argv[j]))
