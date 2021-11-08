import sys

times = int(sys.stdin.readline())

array = [list(map(int,sys.stdin.readline().split())) for i in range(times)]
# min_height = 101
# max_height = 0
# num_secure_area = [list(map(lambda x : 0,range(times**2))) for i in range(101)]
num_secure_area = [0]*101
# for i in array:
#     if min(i) < min_height:
#         min_height = min(i)
#     if max(i) > max_height:
#         max_height = max(i)

 

for height in range(1,101):
    
    counting_arr = [ list(map(lambda x: 1 if x > height else 0,array[i])) for i in range(times)]

    counting = 0
    #counting_arr 합산
    for i in range(times-1):    
        for m in range(times):
            if(counting_arr[i+1][m] >= 1 and counting_arr[i][m]>=1):
                counting_arr[i][m] += 1
    for i in range(times-1,-1,-1):
        for m in range(times):
            if(counting_arr[i-1][m] >= 1 and counting_arr[i][m]>=1):
                counting_arr[i][m] += 1
        
    for j in range(times):
        for k in range(times-1):
            if counting_arr[j][k+1] >= 1 and counting_arr[j][k] >= 1:
                counting_arr[j][k] += 1
        for k in range(times-1,-1,-1):    
            if counting_arr[j][k-1] >= 1 and counting_arr[j][k] >= 1:
                counting_arr[j][k] += 1
    
    #counting_arr 역산
    for i in range(times):
        if i != times-1:
            for j in range(times):
                if j != times-1:
                    if counting_arr[i][j] == 1:
                        counting_arr[i][j] = 5
                    elif counting_arr[i][j] == 0:
                        counting_arr[i][j] = -1
                    else:
                        counting_arr[i][j] -= 1
                        if counting_arr[i][j+1] != 0:
                            counting_arr[i][j+1] -= 1
                        elif counting_arr[i+1][j] != 0:
                            counting_arr[i+1][j] -= 1
                else:
                    if counting_arr[i][j] == 1:
                        counting_arr[i][j] = 5
                    elif counting_arr[i][j] == 0:
                        counting_arr[i][j] = -1
                    else:
                        counting_arr[i][j] -= 1
                        if counting_arr[i+1][j] != 0:
                            counting_arr[i+1][j] -= 1
        else:
            for j in range(times):
                if j != times-1:
                    if counting_arr[i][j] == 1:
                        counting_arr[i][j] = 5
                    elif counting_arr[i][j] == 0:
                        counting_arr[i][j] = -1
                    else:
                        counting_arr[i][j] -= 1
                        if counting_arr[i][j+1] != 0:
                            counting_arr[i][j+1] -= 1
                else:
                    if counting_arr[i][j] == 1:
                        counting_arr[i][j] = 5
                    elif counting_arr[i][j] == 0:
                        counting_arr[i][j] = -1
                    else:
                        counting_arr[i][j] = -1

    
    for i in range(times-1,-1,-1):
        if i != 0:
            for j in range(times-1,-1,-1):
                if j != 0:
                    if counting_arr[i][j] == 5:
                        counting += 1
                    elif counting_arr[i][j-1] == -1 and counting_arr[i+1][j] == -1:
                        counting += 1
                    else:
                        pass
                else:
                    if counting_arr[i][j] == 5:
                        counting += 1
                    elif counting_arr[i][j] == -1:
                        pass
                    else:
                        if counting_arr[i][j-1] == -1 and counting_arr[i+1][j] == -1:
                            pass
        else:




# counting_arr = [[1,0,1],
#                 [0,1,1],
#                 [1,1,1]]
# for i in range(3):
#     if i !=2:
#         for m in range(3):
#             if(counting_arr[i+1][m] >= 1 and counting_arr[i][m]>=1):
#                 counting_arr[i][m] += 1
#     else:
#         for m in range(3):
#             if(counting_arr[i-1][m] >= 1 and counting_arr[i][m]>=1):
#                 counting_arr[i][m] += 1    
# print(counting_arr)