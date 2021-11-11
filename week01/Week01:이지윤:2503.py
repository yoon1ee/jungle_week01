import sys
from itertools import combinations

n = int(sys.stdin.readline())

tmp = list(list(map(int, sys.stdin.readline().split())) for i in range(n))
num = list()

tmp.sort(key=lambda x: x[1], reverse=True)
print(tmp)

for i in tmp:
    strikes = list(combinations(list(str(i[0])), i[1]))
    balls = list(combinations(list(str(i[0])), i[2]))
    print(strikes)
    print(balls)
    i[0]
    break

