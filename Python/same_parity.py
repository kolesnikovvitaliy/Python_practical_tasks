def same_parity(nums):
    return [i for i in nums if nums[0] % 2 == i % 2]
    #nums = list(filter(lambda x: nums[0] % 2 == x % 2, nums))
    #return nums
#print(same_parity([2, 4, 6, 9]))
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))