class Solution:
    def singleNumber(self, nums):
        if not nums or len(nums) <= 0:
            return None

        bitCount = [0] * 32
        for num in nums:
            bitMask = 1
            for j in range(31, -1, -1):
                if num & bitMask != 0:
                    bitCount[j] += 1
                bitMask = bitMask << 1

        result = 0
        for i in range(32):
            result = result << 1
            result += bitCount[i] % 3

        return result
