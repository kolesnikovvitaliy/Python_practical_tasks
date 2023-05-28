def более_одного(lst):
    return " ".join(list(map(str,sorted(list(map(int, set(i for i in lst if lst.count(i) > 1)))))))
lst = input().split()
print(более_одного(lst))
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))