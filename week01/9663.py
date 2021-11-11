import sys

n = int(sys.stdin.readline())

row = [0]*n
print(row)
count = 0

# row = [0]*N
# result = 0

# def adjacent(x): # x와 i 가 같으면 행이 같은거 근데 for문을 보면 x와 i가 같을 수가 없다.
#     for i in range(x): #인덱스가 행  row[n]값이 열
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
#             return False # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
#     return True
 
# #한줄씩 재귀하며 dfs 실행
 
# def dfs(x):
#     global result
 
#     if x == N:
#         result += 1
#     else:
#         # 각 행에 퀸 놓기
#         for i in range(N): # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기 (x, i) 퀸의 위치
#             row[x] = i
#             if adjacent(x): # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
#                 dfs(x + 1)
 
# # N = int(input())/
# row = [0] * N
# result = 0
# dfs(0)
# # print(row)
# print(result)



def adjacent(x):
    for i in range(x):
        #e.g. 3열의 x행에 queen을 두려할 때, 1, 2열의 이미 놓아진 queen 과 겹치는 동선이 없는지 체크
        if row[x] == row[i] or row[x] - row[i] == x - i or row[x]-row[i] == i-x:  # 양,음 -> 좌, 우 대각선
            return False
    return True

def dfs(x):
    global count
    
    if x == n: #마지막 queen까지 다 놓은 상태 queen #0 ~ n-1
        count += 1
    else:
        for i in range(n): #열-세로는 x로 fixed, 행-가로를 하나씩 대조
            #8개의 queen을 8*8체스판에 두려면 한 열에 하나의 queen 이 들어가야되기때문에 
            #하나의 x값(열-세로) 에 여러 i값 test
            row[x] = i
            if adjacent(x):
                #대각선 테스트
                dfs(x+1)

dfs(0)
print(count)







# row = [0]*n
# count = 0

# def listing(n):
#     global count
#     for i in range(n):
#         row[n] = i
#         for j in range(n):
#             if row[n] == row[i] or abs(row[n]-row[i]) == n-i:
#                 listing(n+1)
#             else:
#                 count += 1

# for i in range(n):
#     listing(i)
# print(count)