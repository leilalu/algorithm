"""
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

"""


class Solution:
    def search(self, nums, target):
        if not nums or len(nums) <= 0:
            return 0
        left = self.getLeft(nums, target)
        right = self.getRight(nums, target)
        if left == right == -1:
            return 0
        else:
            return right - left + 1

    def getLeft(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def getRight(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid+1] > target:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
