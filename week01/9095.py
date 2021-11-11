import sys
from itertools import permutations

n = int(sys.stdin.readline())
tmp = [int(sys.stdin.readline()) for i in range(n)]
print(tmp)
# elements = [1, 2, 3]
# count = 0
# for i in tmp: # i = sum up to 
#     for d in range(1, n+1): # d = 각 숫자별 사용 횟수 max = 1 * n
#         n - 1*d
#         options = permutations(elements, d)
#         for e in options:
#             if sum(e) == 
#             count += 1
#     print(count)

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return func(n-1)+func(n-2)+func(n-3)

for i in tmp:
    print(func(i))