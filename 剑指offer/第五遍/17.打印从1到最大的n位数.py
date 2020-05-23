"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数

"""

"""
最大的n位数可能会超出存储范围，因此需要用字符串来保存这些数字，并且模拟加法运算
打印数字时要从第一个非0数字开始
当第一位数字发生进位时，模拟加法结束

"""


class Solution1:
    def printNumbers(self, n):
        # 首先判断输入是否合法
        if n < 1:
            return []

        res = []
        num = ['0'] * n

        while not self.Increment(num):
            # 打印num，加入res中
            number = int(self.PrintNum(num))
            res.append(number)

        return res


    def Increment(self, num):
        circle = 0
        length = len(num) # n
        isOverflow = False
        for i in range(length-1, -1, -1):
            sumValue = circle + int(num[i])  # 计算每一位的和

            # 如果是最后一位，还要加1
            if i == length-1:
                sumValue += 1

            # 计算是否有进位
            if sumValue >= 10:
                # 如果是第一位要进位，则结束
                if i == 0:
                    isOverflow = True
                    break
                else:
                    sumValue -= 10
                    circle = 1
                    num[i] = str(sumValue)

            else:
                num[i] = str(sumValue)
                break

        return isOverflow

    def PrintNum(self, num):
        for i in range(len(num)):
            if num[i] != '0':
                return ''.join(num[i:])


class Solution2:
    def printNumbers(self, n):
        if n < 1:
            return []
        self.res = []
        num = ['0'] * n

        for i in range(10):
            num[0] = str(i)
            self.printNumbersCore(num, n, 0)

        # 从1开始打印，0要舍去
        return self.res[1:]

    def printNumbersCore(self, num, length, index):
        if index == length-1:
            self.res.append(self.PrintNum(num))
            return

        for i in range(10):
            num[index+1] = str(i)
            self.printNumbersCore(num, length, index+1)

    def PrintNum(self, num):
        for i in range(len(num)):
            if num[i] != '0':
                return int(''.join(num[i:]))


if __name__ == '__main__':
    n = 1
    res = Solution2().printNumbers(n)
    print(res)






