"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的【相对位置】不变。

"""


class Solution1:
    def reOrderArray(self, array):
        """
        暴力法，读取两遍数组，并用额外的空间保存新数组，第一遍读奇数，第二遍读偶数
        :param array:
        :return:
        """

        if not array or len(array) == 0:
            return []
        new_array = []
        # 遍历奇数
        for i in range(len(array)):
            if array[i] & 0x1 == 1:
                new_array.append(array[i])

        # 如果全是奇数或全是偶数，则只需要遍历一次即可
        if len(new_array) == 0 or len(new_array) == len(array):
            return array

        # 遍历偶数
        for i in range(len(array)):
            if array[i] & 0x1 == 0:
                new_array.append(array[i])

        return new_array


class Solution2:
    def reOrderArray(self, array):
        """
        看到【数组】，要想起【双指针】
            这道题的关键在于将奇数放在数组的前半部分，将偶数放在数组的后半部分，所有的奇数都在偶数前面，因此在扫描数组的时候，一旦发现
            偶数在奇数前面，就交换奇数和偶数的位置，但是这样【不能保证奇数之间的相对位置和偶数之间的相对位置】

        :param array:
        :return:
        """

        if not array or len(array) == 0:
            return []
        begin = 0
        end = len(array) - 1
        while begin < end:
            # 向后移动begin直到它指向偶数
            while array[begin] & 0x1 != 0 and begin < end:  # 不是偶数
                begin += 1
            while array[end] & 0x1 == 0 and begin < end:  # 是偶数
                end -= 1

            if begin < end:
                # temp = array[begin]
                # array[begin] = array[end]
                # array[end] = temp
                array[begin], array[end] = array[end], array[begin]

        return array


# 可扩展的方法
class Solution3:
    def reOrderArray(self, array):
        """
        将重排数组和判断是否是奇数、偶数分为两个部分：
            1、重排数组：只需要满足某个条件后交换两个指针的内容
            2、判断条件

        """
        if not array or len(array) == 0:
            return []
        begin = 0
        end = len(array) - 1
        while begin < end:
            while begin < end and not self.isEven(array[begin]):
                begin += 1
            while begin < end and self.isEven(array[end]):
                end -= 1

            if begin < end:
                temp = array[begin]
                array[begin] = array[end]
                array[end] = temp

        return array

    def isEven(self, n):
        return n & 1 == 0


class Solution4:
    def reOrderArray(self, array):
        # 利用python的trick
        odd = [x for x in array if x & 1]
        even = [x for x in array if not x & 1]
        return odd + even


if __name__ == '__main__':
    array = [1,2,3,4,5]
    s = Solution4()
    res = s.reOrderArray(array)
    print(res)