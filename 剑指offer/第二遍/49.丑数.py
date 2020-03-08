"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

"""


class Solution1:
    def nthUglyNumber(self, n):
        if n <= 0:
            return
        i = 0
        count = 0
        while count < n:
            i += 1
            if self.isUglyNumber(i):
                count += 1
        return i

    def isUglyNumber(self, num):
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5

        return True if num == 1 else False


class Solution2:
    def nthUglyNumber(self, n):
        if n <= 0:
            return 0

        uglyNumbers = [1] * n
        nextIndex = 1

        index2 =0
        index3 = 0
        index5 = 0

        while nextIndex < n:
            min = self.Min(uglyNumbers[index2] * 2, uglyNumbers[index3] * 3, uglyNumbers[index5] * 5)
            uglyNumbers[nextIndex] = min

            while uglyNumbers[index2] * 2 <= uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3] * 3 <= uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5] * 5 <= uglyNumbers[nextIndex]:
                index5 += 1

            nextIndex += 1

        return uglyNumbers[-1]

    def Min(self, number1, number2, number3):
        if number1 < number2:
            min = number1
        else:
            min = number2

        if min > number3:
            min = number3

        return min


if __name__ == '__main__':
    n = 1
    res = Solution2().nthUglyNumber(n)
    print(res)
