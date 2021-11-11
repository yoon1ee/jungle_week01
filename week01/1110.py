import sys

n = sys.stdin.readline().strip()
tmp = str(n)
# if len(tmp) == 1:
#     tmp.insert(0, 0)
#     keep = tmp[-1]
#     tmp = list(map(int, tmp))
#     tmp = str(sum(tmp))

count = 0
def func(x):
    global count
    count += 1
    tmp = list(str(x))
    if len(tmp) == 1:
        tmp.insert(0,0)
    keep = tmp[-1]
    tmp = list(map(int, tmp))
    tmp_val = str(sum(tmp))
    tmp = str(tmp_val)
    keep_2 = tmp[-1]
    ans = int(keep + keep_2)
    # return ans
    if ans == int(n):
        print(count)
    else:
        func(ans)


func(n)


# count = 1
# final = 0
# while final != n:
#     func(final)


