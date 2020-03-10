"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45

"""


class Solution:
    def sumNums(self, n):
        """"
            可以用递归进行累加，但是递归怎么停止
            递归出口是计算f(0) = 0

        """

        return self.sumN(n)

    def sum0(self, n):
        return 0

    def sumN(self, n):
        func = {True: self.sumN, False: self.sum0}

        return n + func[not not n](n-1)


if __name__ == '__main__':
    n = 3
    res = Solution().sumNums(n)
    print(n)
