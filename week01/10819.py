from itertools import permutations

n = int(input())
given = list(map(int, input().split()))

order = permutations(given)
max_val = 0
for i in order:
    tmp = 0
    for d in range(n-1):
        tmp += abs(i[d-1]-i[d])
    if max_val < tmp:
        max_val = tmp
print(max_val)
    









# from itertools import permutations
# import sys

# n = int(sys.stdin.readline())
# given = list(map(int, sys.stdin.readline().split()))
# options = permutations(given)
# total = 0
# for i in options:
#     tmp = 0
#     for d in range(n-1):
#         tmp += abs(i[d]-i[d+1])
#         if total < tmp:
#             total = tmp
# print(total)