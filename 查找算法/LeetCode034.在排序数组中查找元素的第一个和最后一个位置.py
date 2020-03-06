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


class Solution:
    def searchRange(self, nums, target):
        left = right = -1
        if not nums:
            return [left, right]

        left = self.getLeft(nums, target)
        right = self.getRight(nums, target)
        return [left, right]

    def getLeft(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    high = mid- 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def getRight(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid+1] > target:
                    return mid
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    nums = [3,3,3]
    target = 1
    res = Solution().searchRange(nums, target)
    print(res)



