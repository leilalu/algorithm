"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

斐波那契数列：0、1、1、2、3、5、8、13、21、34  f(n) = f(n-1) + f(n-2)

"""


class Solution:
    def Fibonacci_1(self, n):
        """
        递归法求斐波那契数列的第n项
        会超时

        :param n:
        :return:
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            return self.Fibonacci_1(n - 1) + self.Fibonacci_1(n - 2)

    def Fibonacci_2(self, n):
        """
        不使用递归实现斐波那契数列：第n个元素前面的两个数字存在一个temp数组中，每次计算更新这个数组即可。
        可以通过n % 2控制对temp数组的元素进行更新

        :param n:
        :return:
        """
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i % 2] = tempArray[0] + tempArray[1]
        return tempArray[n % 2]


if __name__ == '__main__':
    s = Solution()
    n = 5
    res = s.Fibonacci_1(n)
    print(res)

