import sys
n, x = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
ans = []
for i in tmp:
    if i < x:
        ans.append(i)
for i in range(x-1):
    print(ans[i], end=" ")


# n = int(input())

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# for i in range(1, 21):
#     print(fibo(i))