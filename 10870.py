import sys
n, x = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
ans = []
for i in tmp:
    if i < x:
        ans.append(i)
for i in range(x-1):
    print(ans[i], end=" ")