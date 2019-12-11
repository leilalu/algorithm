def threeSum(nums):
    res = []
    # 首先对数组进行排序
    nums.sort()

    for k in range(len(nums) -2):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k-1]:
            continue

        i, j = k+1, len(nums)-1

        while i < j:
            s = nums[k]+nums[i]+nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1

    return res

nums = [0,0,0]
print(threeSum(nums))


