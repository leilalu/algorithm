"""
题目描述
输入数字n，按顺序打印出从1到最大的n位十进制数。
比如，输入3，则打印出1，2，3一直到最大的3位数999

"""


class Solution:
    def print1ToMaxOfNDigits_1(self, n):
        # 首先判断输入合法
        if n <= 0:
            return
        numbers = ['0'] * n
        while not self.Increment(numbers):
            self.PrintNumber(numbers)


    def Increment(self, numbers):
        isOverFlow = False
        circle = 0
        length = len(numbers)

        for i in range(length-1, -1, -1):
            nSum = int(numbers[i]) + circle
            if i == length - 1:
                nSum += 1
            if nSum >= 10:
                if i == 0:
                    isOverFlow = True
                else:
                    nSum -= 10
                    circle = 1
                    numbers[i] = str(nSum)
            else:
                numbers[i] = str(nSum)
                break
        return isOverFlow

    def PrintNumber(self, numbers):
        isBeginning0 = True
        for i in range(len(numbers)):
            if isBeginning0 and numbers[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c' % numbers[i], end='')
        print('')

    def print1ToMaxOfNDigits_2(self, n):
        if n <= 0:
            return
        numbers = ['0'] * n
        for i in range(10):
            numbers[0] = str(i)  # '0' - '9'
            self.Print1ToMaxOfNDigitsRecursively(numbers, n, 0)

    def Print1ToMaxOfNDigitsRecursively(self, numbers, length, index):
        if index == length - 1:
            self.PrintNumber(numbers)
            return
        for i in range(10):
            numbers[index+1] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(numbers, length, index+1)


if __name__ == '__main__':
    n = 2
    s = Solution()
    res = s.print1ToMaxOfNDigits_2(n)
    print(res)

