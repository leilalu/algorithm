"""
题目：

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶……也可以跳上n级台阶，此时青蛙跳上一个n级台阶纵沟有多少种跳法？

"""


class Solution:
    def Jump(self, n):
        """"
            用数学归纳法求的 f(n) = 2^(n-1)
        """
        if n <= 0:
            return 1
        
        res = 1
        for i in range(1, n):
            res *= 2
        return res


if __name__ == '__main__':
    n = 2
    res = Solution().Jump(n)
    print(res)
