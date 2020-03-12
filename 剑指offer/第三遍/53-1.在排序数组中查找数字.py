class Solution:
    def search(self, nums, target):
        if not nums or len(nums) <= 0:
            return 0
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        if left == right == -1:
            return 0
        else:
            return right - left + 1

    def searchLeft(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def searchRight(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
