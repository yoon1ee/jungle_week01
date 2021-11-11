import sys

m, d  = map(int, sys.stdin.readline().split())

options = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
a = [1, 3, 5, 7, 8, 10, 12]

def which_day(m, d):
    for i in range(1, m):
        if i in a:
            d += 31
        elif i == 2:
            d+= 28
        else:
            d += 30
            
    print(options[d%7-1])

which_day(m, d)