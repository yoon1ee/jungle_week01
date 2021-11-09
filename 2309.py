import sys

tmp  = [ int(sys.stdin.readline()) for i in range(9) ]
for i in range(9):
    copy = list()
    for x in tmp:
        copy.append(x)
    del copy[i]
    for d in range(8):
        if sum(copy)-copy[d] == 100:
            copy[d]
            for i in copy:
                print(i)
                break