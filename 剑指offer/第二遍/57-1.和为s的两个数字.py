"""
输入一个【递增排序】的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

"""


class Solution:
    def twoSum(self, nums, target):
        if not nums or len(nums) <= 0:
            return []

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []

if __name__ == '__main__':
    nums = [11]
    target = 7

    res = Solution().twoSum(nums, target)
    print(res)

