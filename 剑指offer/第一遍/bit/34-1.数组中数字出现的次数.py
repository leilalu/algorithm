"""
题目一：数组中只出现一次的两个数字

一个整形数组里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现了一次的数字。

要求时间复杂度是O(n)，空间复杂度是O(1)

"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # 检查无效输入
        if not array or len(array) <= 0:
            return []

        resultExclusiveOr = 0
        # 依次异或数组中的每个数
        for i in array:
            resultExclusiveOr ^= i

        # 找到异或结果中第一个1的索引位置
        indexOf1 = self.FindFirstBitIs1(resultExclusiveOr)

        num1, num2 = 0
        for j in range(len(array)):
            if self.IsBit1(array[j], indexOf1):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return [num1, num2]

    # 找到最右边是1的位
    def FindFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0 and indexBit <= 32:
            indexBit += 1
            num = num >> 1
        return indexBit

    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1


class Solution2:
    def FindNumsAppearOnce(self, array):
        # 检查无效输入
        if not array or len(array) <= 0:
            return []
        # 得到数组异或结果
        resultExOr = self.ExOr(array)

        # 找出左数第一个1的位置i
        i = 0
        while resultExOr and i <= 32:
            i += 1
            resultExOr = resultExOr >> 1

        num1, num2 = [], []
        for num in array:
            if self.bitIs1(num, i):
                num1.append(num)
            else:
                num2.append(num)

        first = self.ExOr(num1)
        second = self.ExOr(num2)
        return [first, second]

    # 对数组进行异或
    def ExOr(self, aList):
        ExOrNum = 0
        for i in aList:
            ExOrNum = ExOrNum ^ i
        return ExOrNum

    def bitIs1(self, n, i):
        n = n >> (i-1)
        return n & 1
