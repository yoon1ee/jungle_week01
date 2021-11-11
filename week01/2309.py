# import sys

# tmp  = [ int(sys.stdin.readline()) for i in range(9) ]
# copy = list()
# for i in range(9):
#     if len(copy) == 7:
#         break
#     copy = list()
#     for x in tmp:
#         copy.append(x)
#     del copy[i]
#     for d in range(8):
#         if sum(copy)-copy[d] == 100:
#             del copy[d]
#             copy.sort()
#             for i in copy:
#                 print(i)
#             break
        


import sys

heights = [sys.stdin.readline() for _ in range(9)]
heights = list(map(int, heights))
goal = sum(heights)-100
print("heights", sum(heights))
print("goal", goal)
end = 0
for i in range(8):
    # if end == 1:
    #     break
    for d in range(i+1, 9):
        # if end == 1:
        #     break
        if heights[i]+heights[d] == goal:
            print(heights[i], heights[d])
            a = heights[i]
            b = heights[d]
            heights.remove(a)
            heights.remove(b)
            print("**height", heights)
            heights.sort()
            
            for i in heights:
                sys.stdout.write((str(i) + '\n'))
            sys.exit()