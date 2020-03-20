"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]


说明：

用返回一个整数列表来代替打印
n 为正整数

"""


class Solution1:
    def printNumbers(self, n):
        if n <= 0:
            return []

        res = []
        num = ['0'] * n

        while not self.Increment(num):
            res.append(self.PrintNumber(num))

        return res

    def Increment(self, num):
        isOverflow = False
        circle = 0
        length = len(num)

        for i in range(length-1, -1, -1):
            sumValue = circle + int(num[i])

            if i == length - 1:
                sumValue += 1

            if sumValue >= 10:
                if i == 0:
                    isOverflow = True
                else:
                    sumValue -= 10
                    circle = 1
                    num[i] = str(sumValue)
            else:
                num[i] = str(sumValue)
                # 不会产生进位之后就不要再继续算了！！！！！！
                break

        return isOverflow

    def PrintNumber(self, num):
        for i in range(len(num)):
            if num[i] != '0':
                res = ''.join(num[i:])
                return int(res)
        return


class Solution2:
    def printNumbers(self, n):
        """"
            全排列
        """
        if n <= 0:
            return []

        nums = ['0'] * n
        self.res = []
        for i in range(10):
            nums[0] = str(i)
            self.printNumbersCore(nums, n, 0)

        return self.res[1:]

    def printNumbersCore(self, nums, length, index):
        if index == length-1:
            self.res.append(self.PrintNumber(nums))
            return

        for i in range(10):
            nums[index+1] = str(i)
            self.printNumbersCore(nums, length, index+1)

    def PrintNumber(self, nums):
        for i in range(len(nums)):
            if nums[i] != '0':
                res = ''.join((nums[i:]))
                return int(res)


if __name__ == '__main__':
    n = 1
    res = Solution2().printNumbers(n)
    print(res)



