from itertools import combinations
import sys

def given():
    n = list(map(int, sys.stdin.readline().split()))
    while n != [0]:
        k = n.pop(0)
        options = list(combinations(n, 6))
        for i in options:
            for d in i:
                if d == i[-1]:
                    print(d, end="\n")
                else:
                    print(d, end=" ")
        print()
        n = list(map(int, sys.stdin.readline().split()))
    return
   
given()
