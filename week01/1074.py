# import sys

# n, r, c = map(int, sys.stdin.readline().split())
# ans = 0
# while n != 0:
#     n = n - 1
#     if r < 2 ** n and c < 2 ** n:
#         ans = ans + (2 ** n) * (2 ** n) * 0
#     elif r < 2 ** n <= c:
#         ans = ans + (2 ** n) * (2 ** n) * 1
#         c = c - (2 ** n)
#     elif r >= 2 ** n > c:
#         ans = ans + (2 ** n) * (2 ** n) * 2
#         r = r - (2 ** n)
#     else:
#         ans = ans + (2 ** n) * (2 ** n) * 3
#         r = r - (2 ** n)
#         c = c - (2 ** n)
# print(ans)





import sys
from typing import Counter

n, r, c = map(int, sys.stdin.readline().split())


def find_z(n, r, c):
    side = int(2**n)
    middle = int(side/2)
    global count
    count += 1
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
    print(quadrant*(2**count), r, c, count)
    if side > 2:
        print("side", n-1)
        find_z(n-1, r, c)

count = 0
find_z(n, r, c)

