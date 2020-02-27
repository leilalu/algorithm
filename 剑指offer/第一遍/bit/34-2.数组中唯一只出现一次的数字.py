"""
题目描述

一个整型数组里除了两个数字之外，其他的数字都出现了三次。请写程序找出这两个只出现一次的数字。

"""


class Solution:
    def FindNumberAppearing(self, numbers):
        if not numbers or len(numbers) <= 0:
            return None

        bitSum = [0] * 32
        for i in range(len(numbers)):
            bitMask = 1
            for j in range(31, -1, -1):
                bit = numbers[i] & bitMask
                if bit != 0:
                    bitSum[j] += 1
                bitMask = bitMask << 1

        result = 0
        for i in range(32):
            result = result << 1
            result += bitSum[i] % 3

        return result

