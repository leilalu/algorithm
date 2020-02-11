"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

"""


class Solution:
    def Fibonacci_1(self, n):
        """
            暴力法：斐波那契数列定义
            递归法，会超时

            时间复杂度是n的指数次

        :param n:
        :return:
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            return self.Fibonacci_1(n-1) + self.Fibonacci_2(n-2)

    def Fibonacci_2(self, n):
        """
            由于斐波那契数列是前两个元素之和，因此使用一个长度为2的数组保存将前两个元素保存起来，依次更新这两个元素
            可以通过n % 2控制对temp数组的元素进行更新

            时间复杂度是O(n)

        :param n:
        :return:
        """
        temp = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                    temp[i % 2] = temp[0] + temp[1]
        return temp[n % 2]


if __name__ == '__main__':
    n = 5
    s = Solution()
    res = s.Fibonacci_2(n)
    print(res)



