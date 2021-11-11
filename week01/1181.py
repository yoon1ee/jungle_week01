import sys

n = int(sys.stdin.readline()) 
tmp = [sys.stdin.readline().strip() for i in range(n)]
tmp = list(set(tmp))
tmp.sort()

a = list()
for index, value in enumerate(tmp):
    s = list(value)
    a.append((index, len(s), s[0]))
a.sort(key=lambda x: x[1])
for i in a:
    print(tmp[i[0]])