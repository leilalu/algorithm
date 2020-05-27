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

"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        # 首先判断非法输入
        if not nums or len(nums) <= 0 or k < 1:
            return []

        res = []
        index = []

        if k <= len(nums):
            # 首先加入第一个滑动窗口
            for i in range(k):
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                index.append(i)

            # 窗口滑动
            for i in range(k, len(nums)):
                res.append(nums[index[0]])
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                if index and i - index[0] >= k:
                    index.pop(0)

                index.append(i)

            res.append(nums[index[0]])

        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = Solution().maxSlidingWindow(nums, k)
    print(res)







