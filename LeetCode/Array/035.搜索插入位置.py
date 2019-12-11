"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0

"""


class Solution:
    def searchInsert_1(self, nums, target):
        """
        暴力法查找，一个一个比对
        :param nums: 排序数组
        :param target: 目标值
        :return: 目标值插入排序数组的索引位置
        """
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for index, num in enumerate(nums):
                if target == num:
                    return index
                elif num < target < nums[index+1]:
                    return index + 1

    def searchInsert_2(self, nums, target):
        """
        看到已知数组是排序数组时，要立刻想到使用二分查找来解决。

        首先确定搜索空间，返回的索引取值范围为[0, len(nums)]
        因此left = 0, right = len(nums)

        再看空间收缩，因为当 nums[mid] < target时，答案肯定不会取mid的，答案在mid右边，因此left应该取mid+1
        故为左侧边界收缩，右边界不变，选择左中位数mid = left + (right - left) // 2

        :param nums: 排序数组
        :param target: 目标值
        :return: 目标值插入排序数组的索引位置
        """
        left = 0
        right = len(nums)
        if target > nums[-1]:
            return len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                # assert nums[mid] >= target
                right = mid

        return left


if __name__ == '__main__':

    nums = [1,3,5,6]
    target = 7
    solution = Solution()
    res = solution.searchInsert_2(nums, target)
    print(res)



