"""
题目：

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶……也可以跳上n级台阶，此时青蛙跳上一个n级台阶纵沟有多少种跳法？

"""


class Solution:
    def Jump(self, n):
        if n < 0:
            return None
        res = 1
        for i in range(1, n):
            res *= 2

        return res