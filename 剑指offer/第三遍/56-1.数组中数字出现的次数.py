class Solution:
    def singleNumbers(self, nums):
        if not nums or len(nums) <= 0:
            return []

        ExOr = 0
        for num in nums:
            ExOr ^= num

        count = self.indexOfOne(ExOr)

        num1 = num2 = 0
        for num in nums:
            if self.isBitOne(num, count):
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

    def indexOfOne(self, num):
        count = 0
        while num & 1 != 1 and count <= 32:
            count += 1
            num = num >> 1
        return count

    def isBitOne(self, num, count):
        num = num >> count
        return num & 1