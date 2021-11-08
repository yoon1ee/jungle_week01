import sys

n = int(sys.stdin.readline())

if n < 110:
    count = 99
else:
    count = 99
    for i in range(111, n+1):
        tmp = list(str(i))
        d = int(tmp[-1]) - int(tmp[-2])
        while len(tmp) > 1:
            a = tmp.pop()
            if int(a) - int(tmp[-1]) == d:
                continue
            tmp.pop()
            break
        if len(tmp) == 1:
            count += 1     
print(count)

# import sys

# n = int(sys.stdin.readline())

# if n < 110:
#     count = 99
# else:
#     count = 99
#     for i in range(111, n+1):
#         tmp = list(str(i))
#         print("tmp", tmp)
#         d = int(tmp[-1]) - int(tmp[-2])
#         print("d", d)
#         while len(tmp) > 1:
#             a = tmp.pop()
#             print("a", a)
#             if int(a) - int(tmp[-1]) == d:
#                 print(int(a), int(tmp[-1]), d)
#                 continue
#             tmp.pop()
#             break
#         if len(tmp) == 1:
#             print(tmp)
#             count += 1
                    
# print(count)
