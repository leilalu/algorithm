"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums <= 10000

"""


class Solution:
    def singleNumbers(self, nums):
        if not nums or len(nums) <= 0:
            return []

        exor = 0
        for num in nums:
            exor ^= num

        count = self.indexOfOne(exor)

        # 得到的exor是两个不同的数的异或
        num1 = num2 = 0
        for num in nums:
            if self.isBitOne(num, count):
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

    def indexOfOne(self, num):
        count = 0
        while num & 1 != 1 and count < 32:
            count += 1
            num = num >> 1
        return count

    def isBitOne(self, num, count):
        num = num >> count
        return num & 1
