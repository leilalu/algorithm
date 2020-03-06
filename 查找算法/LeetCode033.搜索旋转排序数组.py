"""
假设按照【升序排序】的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

"""


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            # 如果找到数字
            if nums[mid] == target:
                return mid

            # 如果mid在左半段，在左半段的条件是大于第一个数
            if nums[mid] >= nums[left]:
                # 如果target在左半段，right向前收缩
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # 否则target在后半段，left向后移
                else:
                    left = mid + 1

            # 如果mid在右半段
            else:
                # 如果target在右半段，left向前收缩
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # 否则target比mid大，变大在左边
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = Solution().search(nums, target)
    print(res)







