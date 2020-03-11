class Solution:
    def isStraight(self, nums):
        if not nums or len(nums) < 5:
            return False

        countOfZero = 0
        countOfGap = 0

        nums = sorted(nums)

        i = 0
        while nums[i] == 0:
            countOfZero += 1
            i += 1

        small = i
        big = small + 1
        while big < len(nums):
            if nums[small] == nums[big]:
                return False

            countOfGap += nums[big] - nums[small] - 1
            small = big
            big += 1

        return True if countOfZero >= countOfGap else False
