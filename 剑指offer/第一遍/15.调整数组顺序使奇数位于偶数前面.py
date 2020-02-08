"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的【相对位置】不变。

"""


class Solution:
    def reOrderArray_1(self, array):
        """
        暴力法，读取两遍数组，并用额外的空间保存新数组，第一遍读奇数，第二遍读偶数
        :param array:
        :return:
        """

        if not array or len(array) == 0:
            return []
        new_array = []
        for i in range(len(array)):
            if array[i] & 0x1 == 1:
                new_array.append(array[i])
        if len(new_array) == 0 or len(new_array) == len(array):
            return array
        for i in range(len(array)):
            if array[i] & 0x1 == 0:
                new_array.append(array[i])
        return new_array

    def reOrderArray_2(self, array):
        """
        看到数组，要想起双指针
        这道题的关键在于将奇数放在数组的前半部分，将偶数放在数组的后半部分，所有的奇数都在偶数前面，因此在扫描数组的时候，一旦发现
        偶数在奇数前面，就交换奇数和偶数的位置，但是这样不能保证奇数之间的相对位置和偶数之间的相对位置

        :param array:
        :return:
        """

        if not array or len(array) == 0:
            return []
        begin = 0
        end = len(array) - 1
        while begin < end:
            # 向后移动begin直到它指向偶数
            while array[begin] & 0x1 != 0 and begin < end:
                begin += 1
            while array[end] & 0x1 == 0 and begin < end:
                end -= 1

            if begin < end:
                temp = array[begin]
                array[begin] = array[end]
                array[end] = temp

        return array

    def reOrderArray_3(self, array):
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

    def reOrderArray_4(self, array):
        # 利用python的trick
        odd = [x for x in array if x & 1]
        even = [x for x in array if not x & 1]
        return odd + even


if __name__ == '__main__':
    array = [1,2,3,4,5]
    s = Solution()
    res = s.reOrderArray_4(array)
    print(res)