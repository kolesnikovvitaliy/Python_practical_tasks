import itertools as it


wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
print(sum(sum(1 for i in set(it.combinations(wallet, r=j)) if sum(i) == 100) for j in range(1, len(wallet))))
# print(sum(1 for i in range(len(wallet)) for j in set(combinations(wallet, r=i)) if sum(j) == 100))