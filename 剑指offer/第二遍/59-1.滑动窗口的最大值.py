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


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or len(nums) == 0 or k <= 0:
            return []

        if k >= len(nums):
            return [self.getMaxValue(nums, 0, len(nums)-1)]

        begin = 0
        end = begin + k-1
        result = []
        while end <= len(nums)-1:
            result.append(self.getMaxValue(nums, begin, end))
            begin += 1
            end += 1
        return result

    def getMaxValue(self, nums, begin, end):
        if begin == end:
            return nums[begin]

        maxValue = nums[begin]
        for i in range(begin+1, end+1):
            if nums[i] > maxValue:
                maxValue = nums[i]

        return maxValue

class Solution2:
    def maxSlidingWindow(self, nums, k):
        if not nums or k <= 0:
            return []
        # 队列
        result = []
        if k <= len(nums):
            index_queue = []  # 用来存储当前滑动窗口可能的最大值的下标
            for i in range(k):
                while len(index_queue) > 0 and nums[i] >= nums[index_queue[-1]]:
                    index_queue.pop()
                index_queue.append(i)

            for i in range(k, len(nums)):
                result.append(nums[index_queue[0]])
                while len(index_queue) > 0 and nums[i] >= nums[index_queue[-1]]:
                    index_queue.pop()

                if len(index_queue) > 0 and i - index_queue[0] >= k:
                    index_queue.pop(0)

                index_queue.append(i)

            result.append(nums[index_queue[0]])
        return result


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = Solution2().maxSlidingWindow(nums, k)
    print(res)

