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
                if mid == 0 or nums[mid-1] == mid - 1:
                    return mid
                else:
                    right = mid - 1

        if left == len(nums):
            return left

        return None
