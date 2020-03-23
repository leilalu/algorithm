"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or len(nums) <= 0 or k < 1:
            return []
        queue = []
        index = []
        if k <= len(nums):
            for i in range(k):
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                index.append(i)

            for i in range(k, len(nums)):
                queue.append(nums[index[0]])
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                if index and i - index[0] >= k:
                    index.pop(0)
                index.append(i)

            queue.append(nums[index[0]])

        return queue







