"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8

"""


class Solution:
    def missingNumber(self, nums):
        if not nums or len(nums) <= 0:
            return None
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == mid:
                left = mid + 1
            else:
                if mid == 0 or nums[mid - 1] == mid - 1:
                    return mid
                else:
                    right = mid - 1
        if left == len(nums):
            return left
        return None


if __name__ == '__main__':
    nums = [0,1,2,3,4,5,6,7,8]
    res = Solution().missingNumber(nums)
    print(res)
