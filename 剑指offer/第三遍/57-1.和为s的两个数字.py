class Solution:
    def twoSum(self, nums, target):
        if not nums or len(nums) <= 0:
            return []

        begin = 0
        end = len(nums) - 1

        while begin < end:
            if nums[begin] + nums[end] == target:
                return [nums[begin], nums[end]]
            elif nums[begin] + nums[end] > target:
                end -= 1
            elif nums[begin] + nums[end] < target:
                begin += 1

        return []