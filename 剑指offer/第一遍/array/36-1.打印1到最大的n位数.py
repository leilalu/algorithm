"""
题目描述

输入数字n，按顺序打印出从1到最大的n位十进制数。
比如，输入3，则打印出1，2，3一直到最大的3位数999

"""


class Solution1:
    def print1ToMaxOfNDigits(self, n):
        """
            首先注意到这是一个【大数问题】，没有指定n的大小，可能非常非常大，数字超过了存储范围，考虑使用字符串和数组存储数字

            在本题中主要分为两步：
                第一步：用字符数组表示的数字累加1，需要模拟数字的加法，还需要判断是否已经达到最大的n位数：第一位发生进位
                第二步：打印字符数组，从第一个非零数字打印

        """
        # 首先判断输入合法
        if n <= 0:
            return
        # 用数组存放大数 n位数 n个元素
        numbers = ['0'] * n

        # 累加1 并判断是不是已经达到了最大的n位数
        while not self.Increment(numbers):
            # 打印数组
            self.PrintNumber(numbers)

    def Increment(self, numbers):
        """
            数组表示数字累加1，并判断是否到达了最大n位数
        """
        # 标注第一位数字是否进位，若进位为True，则达到最大
        isOverFlow = False
        circle = 0
        length = len(numbers)

        for i in range(length-1, -1, -1):
            # 累加从最后一位开始到第一位，每一位先加进位
            nSum = int(numbers[i]) + circle
            # 如果是最后一位，则加上1，如果不是，则只加进位即可
            if i == length - 1:
                nSum += 1
            # 如果产生新的进位
            if nSum >= 10:
                # 如果是第一位产生了进位，则结束
                if i == 0:
                    isOverFlow = True
                else:
                    nSum -= 10
                    circle = 1
                    numbers[i] = str(nSum)
            # 没有产生新进位
            else:
                numbers[i] = str(nSum)
                # 接下来的位将不需要计算了
                break
        return isOverFlow

    def PrintNumber(self, numbers):
        """
            只有在碰到第一个非零数字时才开始打印

            该函数每次打印的只有一个数，因为每次数组里也只有一个数
        """
        isBeginning0 = True
        for i in range(len(numbers)):
            if isBeginning0 and numbers[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c' % numbers[i], end='')
        print('')


class Solution2:
    def print1ToMaxOfNDigits(self, n):
        """
        n位所有的十进制数，可以看作是n个0到9的全排列。我们可以把每位数字都从0-9进行排列。
        全排列可以通过递归来表达

        """
        if n <= 0:
            return
        numbers = ['0'] * n
        # 第一个数字
        for i in range(10):
            numbers[0] = str(i)  # '0' - '9'
            self.Print1ToMaxOfNDigitsRecursively(numbers, n, 0)

    def Print1ToMaxOfNDigitsRecursively(self, numbers, length, index):
        # 递归退出条件，设置了数字的最后一位
        # 注意，设置了最后一位不代表是一个n位数，有可能是000，只有所有位都设置满了才可以打印
        if index == length - 1:
            self.PrintNumber(numbers)
            return

        for i in range(10):
            numbers[index+1] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(numbers, length, index+1)

    def PrintNumber(self, numbers):
        """
            只有在碰到第一个非零数字时才开始打印
        """
        isBeginning0 = True
        for i in range(len(numbers)):
            if isBeginning0 and numbers[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c' % numbers[i], end='')
        print('')


if __name__ == '__main__':
    n = 3
    s = Solution1()
    res = s.print1ToMaxOfNDigits(n)
    print(res)

