def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        ## 앞에서부터 작은 수 정렬 
        for j in range(n-1, i, -1):
            ## 뒤에서부터 작은 수 앞으로 밀어주기 / 큰 수 뒤로 빼주기
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a

a = [6, 4, 3, 7, 1, 9, 8]

print(bubble_sort(a))