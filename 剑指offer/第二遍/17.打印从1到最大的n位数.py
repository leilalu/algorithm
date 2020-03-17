"""
题目描述

输入数字n，按顺序打印出从1到最大的n位十进制数。
比如，输入3，则打印出1，2，3一直到最大的3位数999

"""


class Solution1:
    def Print1ToN(self, n):
        if n <= 0:
            return None

        numbers = ['0'] * n

        while not self.Increment(numbers):
            self.PrintNumber(numbers)

    def Increment(self, numbers):
        isOverflow = False
        circle = 0
        length = len(numbers)

        for i in range(length-1, -1, -1):
            sum = int(numbers[i]) + circle
            if i == length - 1:
                sum += 1

            if sum >= 10:
                if i == 0:
                    isOverflow = True
                else:
                    sum -= 10
                    circle = 1
                    numbers[i] = str(sum)
            else:
                numbers[i] = str(sum)
                # break很重要，接下来不要再计算了
                break

        return isOverflow

    def PrintNumber(self, numbers):
        isBeginning0 = True
        for i in range(len(numbers)):
            if isBeginning0 and numbers[i] != '0':
                isBeginning0 = False

            if not isBeginning0:
                print('%c' % numbers[i], end='')
        print()


class Solution2:
    def Print1ToN(self, n):
        if n <= 0:
            return

        numbers = ['0'] * n

        # 设置第一位
        for i in range(10):
            numbers[0] = str(i)
            self.Print1ToNCore(numbers, n, 0)

    def Print1ToNCore(self, numbers, length, index):
        if index == length - 1:
            self.PrintNumber(numbers)
            return
        for i in range(10):
            numbers[index+1] = str(i)
            self.Print1ToNCore(numbers, length, index+1)

    def PrintNumber(self, numbers):
        isBeginning0 = True
        for i in range(len(numbers)):
            if isBeginning0 and numbers[i] != '0':
                isBeginning0 = False

            if not isBeginning0:
                print('%c' % numbers[i], end='')
        print()



if __name__ == '__main__':
    n = 2
    s = Solution1()
    res = s.Print1ToN(n)
    print(res)








