"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""


class Solution:
    def reOrderArray(self, array):
        if not array or len(array) == 0:
            return []

        begin = 0
        end = len(array)-1

        while begin < end:
            while self.isOdd(array[begin]) and begin < end:
                begin += 1
            while not self.isOdd(array[end]) and begin < end:
                end -= 1

            if begin < end:
                array[begin], array[end] = array[end], array[begin]
        return array

    def isOdd(self, num):
        return num & 1 == 1
