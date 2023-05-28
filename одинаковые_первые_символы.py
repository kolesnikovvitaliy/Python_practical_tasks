s = input().split(',')
print(s)
count = 0
a = [j for i in range(len(s)) for j in s[i]]

b = []
#b = [a[i] for i in range(len(a)) if a.count(a[i]) == len(s)]
for i in range(len(a)):
    if a.count(a[i]) != len(s):
        break
    else:
        b.append(a[i])

print(''.join(b))
