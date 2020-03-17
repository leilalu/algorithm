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
        if n < 1:
            return []

        res = []
        nums = ['0'] * n

        while not self.Increment(nums):
            print(nums)
            number = int(self.PrintNumber(nums))
            res.append(number)
        return res

    def Increment(self, nums):
        length = len(nums)
        circle = 0
        isOverlfow = False
        for i in range(length-1, -1, -1):
            sumValue = circle + int(nums[i])
            if i == length - 1:
                sumValue += 1
            if sumValue >= 10:
                if i == 0:
                    isOverlfow = True
                else:
                    sumValue -= 10
                    circle = 1
                    nums[i] = str(sumValue)

            else:
                nums[i] = str(sumValue)
                # 接下来不要再算了！！！！
                break

        return isOverlfow

    def PrintNumber(self, nums):
        for i in range(len(nums)):
            if nums[i] != '0':
                return ''.join(nums[i:])


class Solution2:
    def printNumbers(self, n):
        if n <= 0:
            return

        self.res = []
        nums = ['0'] * n
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
                return int(''.join(nums[i:]))

if __name__ == '__main__':
    n = 3
    res = Solution2().printNumbers(n)
    print(res)

