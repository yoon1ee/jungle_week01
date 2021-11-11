import sys
from itertools import combinations, permutations

n = int(sys.stdin.readline())
cost_set = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
a = [i for i in range(n)]
min_cost = 1000000001*n
for each_j in permutations(range(n)):
    total_cost = 0
    for index in range(n):
        if index == n-1:
            departure = each_j[index]
            destination = each_j[0]
        else:
            departure = each_j[index]
            destination = each_j[index+1]
        if cost_set[departure][destination] != 0:
            total_cost += cost_set[departure][destination]
        else:
            break
    if total_cost != 0:
        min_cost = min(min_cost,total_cost)
    # if min_cost > total_cost:
    #     min_cost = total_cost
print(min_cost)


        

# import sys

# n = int(sys.stdin.readline())
# tmp = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# # x = destination 열 세로
# # i = departure 행 가로
# def cost(x):
#     mid_journey = list()
#     min_cost = 1000000
#     for i in range(n):
#         print("x", x, "i", i)
#         cost = tmp[i][x-1]
#         if i+1 in des_list:
#             print(i+1, "visited")
#             continue
#         else:
#             print("yet to visit")
#             if min_cost > cost:
#                 if i == x-1:
#                     print("same city")
#                     continue
#                 else:
#                     min_cost = cost
#                     print("new min", min_cost)
#                     mid_journey = [i+1, x, min_cost]
#     journey.append(mid_journey)
#     des_list.append(mid_journey[0])
#     print("journey", journey)
#     print("des_list", des_list)

# journey = list() 
# des_list = list()   
