"""
统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

"""

"""
看到题目中【排序数组】想到使用二分查找找到元素，然后找到最左和最右的元素，就可以得到出现的次数
"""


class Solution:
    def search(self, nums, target):
        # 判断输入是否合法
        if not nums or len(nums) <= 0:
            return 0

        left = self.serch_left(nums, target)
        right = self.search_right(nums, target)

        if left == right == -1:
            return 0
        else:
            return right - left + 1

    def serch_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search_right(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid + 1] != target:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    res = Solution().search(nums, target)
    print(res)

