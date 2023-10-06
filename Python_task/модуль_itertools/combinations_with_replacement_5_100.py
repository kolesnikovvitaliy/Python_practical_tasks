import itertools as it


wallet = [100, 50, 20, 10, 5]
print(sum(sum(1 for i in set(it.combinations_with_replacement(wallet, r=j)) if sum(i) == 100) for j in range(1, 21)))