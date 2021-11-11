import sys
n = int(sys.stdin.readline())
row = [0]*n
count = 0

def listing(x):
    global count
    if x == n:
        count += 1
    else:
        for i in range(n):
            row[x] = i
            for d in range(x):
                if False:
                    
                if row[x] == row[d] or abs(row[x]-row[d]) == x-d:
                    return False
            if False:
                break
            else:
                listing(x+1)                
listing(0)
print(count)

# import sys

# n = int(sys.stdin.readline())
# count = 0
# row = [0]*n

# def adjacent(x):
#     for s in range(x):
#         if row[x] == row[s] or abs(row[x]-row[s]) == x-s:
#             return False
#     return True
    
# def queen(x):
#     global count

#     if x == n:
#         count += 1
#     else:
#         for i in range(n):
#             row[x] = i
#             if adjacent(x):
#                 queen(x+1)
                
# queen(0)
# print(count)