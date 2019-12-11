"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]


"""

def find_left(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            right = mid
        elif target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1

    if left == len(nums):
        return -1

    if nums[left] == target:
        return left
    else:
        return -1


def find_right(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1

    if left == 0:
        return -1

    if nums[left - 1] == target:
        return left - 1
    else:
        return -1


def searchRange(nums, target):

    left = find_left(nums,target)
    right = find_right(nums, target)
    return [left, right]



nums = [5,7,7,8,8,10]
res = searchRange(nums, 6)
print(res)


