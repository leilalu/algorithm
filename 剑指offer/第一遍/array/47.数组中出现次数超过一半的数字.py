"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""
import random


class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        # 检查输入是否合法
        if self.CheckInvalidArray(numbers, length):
            return 0

        if length == 1:
            return numbers[0]

        middle = length >> 1  # 右移一位相当于整除2
        start = 0
        end = length - 1
        index = self.Partition(numbers, start, end)
        while index != middle:
            if index > middle:  # 选中的数大于 n/2
                end = index - 1
                index = self.Partition(numbers, start, end)
            else:
                start = index + 1
                index = self.Partition(numbers, start, end)
        result = numbers[middle]
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result

    # 划分算法
    def Partition(self, array, start, end):
        if start == end:
            # 只有一个数时
            pivot = start
        else:
            pivot = random.randrange(start, end)
        # 先把基准值换到列表的最后一位上
        array[pivot], array[end] = array[end], array[pivot]
        small = start - 1
        for i in range(start, end):
            if array[i] < array[end]:
                small += 1
                if small != i:
                    # 此时 small 指向第一个大于pivot的数，i指向小于pivot的数，将他俩互换
                    array[small], array[i] = array[i], array[small]

        small += 1
        array[small], array[end] = array[end], array[small]

        return small

    # 检查输入的数组是否合法
    def CheckInvalidArray(self, numbers, length):
        InputInvalid = False
        if not numbers or length <= 0:
            InputInvalid = True
        return InputInvalid

    # 检查查找到中位数的元素出现次数是否超过所有元素数量的一半
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True


class Solution2:
    # 根据数组特点找出O(n)的算法
    def MoreThanHalfNum(self, numbers):
        length = len(numbers)
        if not numbers or length <= 0:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result

        # 检查查找到中位数的元素出现次数是否超过所有元素数量的一半

    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True


class Solution3:
    def MoreThanHalfNum(self, nums):
        """
            投票法

        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            count += (1 if num == candidate else -1)

        return candidate