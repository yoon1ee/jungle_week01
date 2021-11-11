import sys

n = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# print(area)
# flood = [[0]*n]*n
# [0]*n 의 변화값이 n행에 모두 적용.. 왜?! 얕은복사?

flood = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

# print(flood)

count = 0
test = list()
def rain(r): # r = 강수량
    for row in range(n):
        for column in range(n):
            # print(row, column)
            if area[row][column] <= r:
                # print(row, column, "=", area[row][column])
                flood[row][column] = 1
            else:
                test.append((row, column))

                # print(flood)

# for i in range(1, 100):
    # rain(i)

rain(6)

print(flood)
print(test)
ans = list()

visited = list()
def if_counted(x, y):
    visited.append((x, y))
    if flood[x-1][y] == 0:
        if (x-1, y) not in visited:
            if_counted(x-1, y)
        
    if flood[x+1][y] == 0:
        if (x-1, y) not in visited:
            if_counted(x-1, y)
    if flood[x][y-1] == 0:
        if (x, y-1) not in visited:
            if_counted(x, y-1)
    if flood[x][y+1] == 0:
        if (x, y+1) not in visited:
            if_counted(x, y+1)



# safe_area = list()
ans = list()
for row in range(n):
    for column in range(n):
        if flood[row][column] == 0:
            if column == 0 and row == 0:
                ans.append((row, column))
                count += 1
            elif row == 0:
                if flood[row][column-1] == 1:
                    if_counted(row, column)
                    ans.append((row, column))
                    count += 1
            elif column == 0:
                if flood[row-1][column] == 1:
                    ans.append((row, column))
                    count += 1
            else:
                if flood[row-1][column] == 1 and flood[row][column-1] == 1:
                    ans.append((row, column))
                    count += 1

print(count)
print(ans)



            
            # if flood[row-1][column] == 0 or flood[row][column-1] == 0:
            #     count += 1
