class Solution:
    def maxValue(self, nums, k):
        if not nums or len(nums) <= 0 or k <= 0:
            return []

        result = []
        if k <= len(nums):
            index_queue = []
            for i in range(k):
                while index_queue and nums[i] >= nums[index_queue[-1]]:
                    index_queue.pop()
                index_queue.append(i)

            for i in range(k, len(nums)):
                result.append(nums[index_queue[0]])
                while index_queue and nums[i] >= nums[index_queue[-1]]:
                    index_queue.pop()

                if index_queue and i - index_queue[0] >= k:
                    index_queue.pop(0)

                index_queue.append(i)

            result.append(nums[index_queue[0]])

        return result