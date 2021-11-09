import sys

# times = int(sys.stdin.readline())

# array = [list(map(int,sys.stdin.readline().split())) for i in range(times)]
# # min_height = 101
# # max_height = 0
# # num_secure_area = [list(map(lambda x : 0,range(times**2))) for i in range(101)]
# num_secure_area = [0]*101
# # for i in array:
# #     if min(i) < min_height:
# #         min_height = min(i)
# #     if max(i) > max_height:
# #         max_height = max(i)

 

# for height in range(1,101):
    
#     counting_arr = [ list(map(lambda x: 1 if x > height else 0,array[i])) for i in range(times)]

#     counting = 0
#     #counting_arr 합산
#     for i in range(times-1):    
#         for m in range(times):
#             if(counting_arr[i+1][m] >= 1 or counting_arr[i][m]>=1):
#                 counting_arr[i][m] += 1
#     for i in range(times-1,-1,-1):
#         for m in range(times):
#             if(counting_arr[i-1][m] >= 1 or counting_arr[i][m]>=1):
#                 counting_arr[i][m] += 1
        
#     for j in range(times):
#         for k in range(times-1):
#             if (counting_arr[j][k+1] >= 1 or counting_arr[j][k] >= 1):
#                 counting_arr[j][k] += 1
#         for k in range(times-1,-1,-1):    
#             if (counting_arr[j][k-1] >= 1 or counting_arr[j][k] >= 1):
#                 counting_arr[j][k] += 1
    
#     #counting_arr 역산
#     for i in range(times):
#         if i != times-1:
#             for j in range(times):
#                 if j != times-1:
#                     if counting_arr[i][j] == 1:
#                         counting_arr[i][j] = 20
#                     elif counting_arr[i][j] == 0:
#                         counting_arr[i][j] = -1
#                     else:
#                         counting_arr[i][j] -= 1
#                         if counting_arr[i][j+1] != 0:
#                             counting_arr[i][j+1] -= 1
#                         elif counting_arr[i+1][j] != 0:
#                             counting_arr[i+1][j] -= 1
#                 else:
#                     if counting_arr[i][j] == 1:
#                         counting_arr[i][j] = 20
#                     elif counting_arr[i][j] == 0:
#                         counting_arr[i][j] = -1
#                     else:
#                         counting_arr[i][j] -= 1
#                         if counting_arr[i+1][j] != 0:
#                             counting_arr[i+1][j] -= 1
#         else:
#             for j in range(times):
#                 if j != times-1:
#                     if counting_arr[i][j] == 1:
#                         counting_arr[i][j] = 20
#                     elif counting_arr[i][j] == 0:
#                         counting_arr[i][j] = -1
#                     else:
#                         counting_arr[i][j] -= 1
#                         if counting_arr[i][j+1] != 0:
#                             counting_arr[i][j+1] -= 1
#                 else:
#                     if counting_arr[i][j] == 1:
#                         counting_arr[i][j] = 20
#                     elif counting_arr[i][j] == 0:
#                         counting_arr[i][j] = -1
#                     else:
#                         counting_arr[i][j] -= 1
#     # for i in counting_arr:
#     #     i = list(map(lambda x : 5 if x == 1 else x , i))

#     #counting_arr 역산 2
#     for i in range(times-1,-1,-1):
#         if i != 0:
#             for j in range(times-1,-1,-1):
#                 if j != 0:
#                     if counting_arr[i][j] == 20:
#                         counting += 1
#                     elif counting_arr[i][j] == -1:
#                         break
#                     elif counting_arr[i][j-1] == -1 and counting_arr[i-1][j] == -1:
#                         counting += 1
#                 else:
#                     if counting_arr[i][j] == 20:
#                         counting += 1
#                     elif counting_arr[i][j] == -1:
#                         break
#                     else:
#                         if counting_arr[i-1][j] == -1:
#                             counting += 1
#         else:
#             for j in range(times-1,-1,-1):
#                 if j != 0:
#                     if counting_arr[i][j] == 20:
#                         counting += 1
#                     elif counting_arr[i][j] == -1 :
#                         break
#                     else:
#                         if counting_arr[i][j-1] == -1:
#                             counting += 1
#                 else:
#                     if counting_arr[i][j] == 20:
#                         counting += 1
#                     else:
#                         counting += 1
#                         break
#     num_secure_area[height] = counting

# print(max(num_secure_area))

#0번 튜플은 마지막값 저장을 위해 삽입
arr = [(0,0),(1,1),(2,1),(3,0),(4,1),(5,0),(6,1)]
arr2 = [(0,0),(1,0),(2,1),(3,1),(4,1),(5,0),(6,1)]
final_area = []
final_area2 =[]
index = []
area = set()
for i in arr[::-1]:
    if i[1] != 0:
        area.add(arr.pop())
        continue
    else:
        del arr[-1]
        if area == set():
            continue
        else:
            final_area.append(area)
            area = set()

for i in arr2[::-1]:
    if i[1] != 0:
        area.add(arr2.pop())
        continue
    else:
        del arr2[-1]
        if area == set():
            continue
        else:
            final_area2.append(area)
            area = set()


for a in final_area2:
    for i in final_area:
        if a.isdisjoint(i) == False:
            index.append(a.union(i))



print(index)
# print()