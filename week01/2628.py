import sys

paper_w, paper_h = map(int, sys.stdin.readline().split())
cut = int(sys.stdin.readline())
tmp = [sys.stdin.readline().split() for i in range(cut)]

width = list()
height = list()
for i in tmp:
    if i[0] == "1":
        width.append(int(i[1]))
    else:
        height.append(int(i[1]))
width.insert(0, 0)
height.insert(0, 0)
width.append(paper_w)
height.append(paper_h)
width.sort()
height.sort()

tmp_w = 0
for r in width[:-1]:
    end = width.pop()
    new_w = end - width[-1]
    if tmp_w < new_w:
        tmp_w = new_w

tmp_h = 0
for r in height[:-1]:
    end = height.pop()
    new_h = end - height[-1]
    if tmp_h < new_h:
        tmp_h = new_h

print(tmp_w * tmp_h)


