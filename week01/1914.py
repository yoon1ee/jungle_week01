import sys

n = int(sys.stdin.readline())

def hanoi(n, x, y):
    if n > 1:
        hanoi(n-1, x, 6-x-y)
    print(x, y)
    if n > 1:
        hanoi(n-1, 6-x-y, y)
print(2**n-1)
if n > 20:
    pass
else:
    hanoi(n, 1, 3)