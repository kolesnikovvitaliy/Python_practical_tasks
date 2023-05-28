def переворатор(n, x, y, a, b):
    
    e = ''
    lst = [i for i in range(1, n+1)]
    lst_1 = lst[:x-1]+lst[x-1:y][::-1]+lst[y:]
    lst_2 = lst_1[:a-1]+lst_1[a-1:b][::-1]+lst_1[b:]
    for i in lst_2:
        e += str(i)
    return int(e)

n, x, y, a, b = map(int, input().split())
print(переворатор(n, x, y, a, b))