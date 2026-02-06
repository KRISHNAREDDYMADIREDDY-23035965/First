def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        print(target,num,diff)
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(two_sum([2,7,11,15], 9))  # [0,1]
