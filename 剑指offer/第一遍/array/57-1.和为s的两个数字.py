"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。

"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """
            【两数之和】的问题

            需要充分利用【数组已经排好序】的特点。使用【双指针】法

            第一个指针指向数组第一个元素，第二个指针指向数组最后一个元素。

            当两指针所指元素之和大于输入数字时，则将第二个指针向前移一位
            当两指针所指元素之和小于输入数字时，则将第一个指针向前移一位

        """

        if not array:
            return []

        start = 0
        end = len(array)-1

        while start < end:
            sum = array[start] + array[end]
            if sum > tsum:
                end -= 1
            elif sum < tsum:
                start += 1
            else:
                return array[start], array[end]

        return []

