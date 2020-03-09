"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1

"""


class Solution:
    def singleNumber(self, nums):
        if not nums or len(nums) <= 0:
            return None
        bitSum = [0] * 32

        for i in range(len(nums)):
            bitMask = 1
            for j in range(31, -1, -1):
                bit = nums[i] & bitMask
                if bit != 0:
                    bitSum[j] += 1
                bitMask = bitMask << 1

        result = 0
        for i in range(32):
            result = result << 1
            result += bitSum[i] % 3
        return result

