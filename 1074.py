import sys

n, r, c = map(int, sys.stdin.readline().split())


def find_z(n, r, c):
    side = int(2**n)
    middle = int(side/2)
    if  middle >= r:
        if middle >= c:
            quadrant = 1
        else:
            quadrant = 2
            c = c-middle
    else:
        if middle >= c:
            quadrant = 3
            r = r-middle
        else:
            quadrant = 4
            r = r-middle
            c = c-middle
    print(r, c)
    if side > 2:
        print("side", n-1)
        find_z(n-1, r, c)

find_z(n, r, c)
