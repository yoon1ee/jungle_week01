import sys

n, m = map(int, sys.stdin.readline().split())

given = list(map(int, sys.stdin.readline().split()))

longest = max(given)

def height(given, h):
    for index in range(len(given)):
        if given[index] >= h:
            tmp = given[index] - h
            given[index] = tmp
        else:
            given[index] = 0
    print("given", given)
    return (sum(given))

ans = 0
for i in range(longest, 1, -1):
    print("height", i)
    if height(given, i) >= n:
        if i > ans:
            ans = i
print(ans)


        

