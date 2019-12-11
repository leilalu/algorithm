def fourSum(nums, target):
    res = []
    nums.sort()

    for k in range(len(nums)-3):
        if k > 0 and nums[k] == nums[k-1]:
            continue
        if nums[k]+nums[k+1]+nums[k+2]+nums[k+3] > target:
            break

        if nums[k]+nums[-3]+nums[-2]+nums[-1] < target:
            continue

        for p in range(k+1, len(nums)-2):
            if p > k+1 and nums[p] == nums[p - 1]:
                continue
            if nums[k] + nums[p] + nums[p + 1] + nums[p + 2] > target:
                break

            if nums[k] + nums[p] + nums[-2] + nums[-1] < target:
                continue

            i, j = p+1, len(nums)-1

            while i < j:
                s = nums[k]+nums[p]+nums[i]+nums[j]
                if s < target:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif s > target:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[p], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

    return res


def fourSum_1(nums, target):
    nums.sort()
    ans = set()

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):  # 固定两个数
            left = j + 1  # 左指针
            right = len(nums) - 1  # 右指针
            while right > left:
                temp = nums[i] + nums[j] + nums[left] + nums[right]
                if temp == target:
                    ans.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                if temp > target: right -= 1  # 太大了，右指针左移
                if temp < target: left += 1  # 反之
    # 去重
    res = []
    for i in ans:
        res.append(list(i))
    return res

nums = [0,0,0,0]
target = 0
res = fourSum_1(nums, target)
print(res)

