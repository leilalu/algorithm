"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

"""


class Solution:
    def twoSum(self, nums, target):
        # 首先判断输入是否合法
        if not nums or len(nums) <= 0:
            return []

        start = 0
        end = len(nums) - 1

        while start <= end:
            sumValue = nums[start] + nums[end]
            if sumValue > target:
                end -= 1
            elif sumValue < target:
                start += 1
            else:
                return [nums[start], nums[end]]

        return []


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 19
    res = Solution().twoSum(nums, target)
    print(res)

