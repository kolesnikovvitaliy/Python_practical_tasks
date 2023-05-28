def максимальная_группа(n):
    #sum(map(int, list(str(x))))
    d = []
    for i in range(1, n + 1):
        d.append(sum(int(j) for j in str(i)))
    
    return max(d.count(i) for i in d)
n = int(input())
print(максимальная_группа(n))