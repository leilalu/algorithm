def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]

    for k in range(len(nums) - 2):
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if abs(target - s) < abs(target - res):
                res = s
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                res = s
                return res

    return res


nums = [-1,2,1,-4]
target = 1

res = threeSumClosest(nums, target)
print(res)