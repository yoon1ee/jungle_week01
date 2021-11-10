n = int(input())
def nQueen(n):
    if(n==1):
        return 1
    elif(n==2):
        return 0
    return nQueen(n-2) + 4

print(nQueen(n))