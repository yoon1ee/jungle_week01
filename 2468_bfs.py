import sys
from collections import deque

times = int(sys.stdin.readline())

array = [list(map(int,sys.stdin.readline().split())) for i in range(times)]

dy =[0,1,0,-1]
dx =[1,0,-1,0]
def bfs (y,x):

    q = deque()
    q.append([y,x])
    while q:
       cy , cx =  q.popleft()
       for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<times and 0<=nx<times:
                if chk[ny][nx] == False and counting_arr[ny][nx] == 1:
                    chk[ny][nx] = True
                    q.append([ny,nx])

mxv = 0
for height in range(0,10):
    chk = [[False] * times for _ in range(times)]
    counting_arr =  [list(map(lambda x: 1 if array[i][x] > height else 0,range(times))) for i in range(times)]
    
    cnt = 0
    for j in range(times):
        for i in range(times):
            if counting_arr[j][i] == 1 and chk[j][i] == False:
                cnt += 1
                chk[j][i] = True
                bfs(j,i)
    # print(counting_arr)
    # print(cnt,mxv,end="     ")
    mxv = max(mxv,cnt)
    # print(mxv)
    

print(mxv)
