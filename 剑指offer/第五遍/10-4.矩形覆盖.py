"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

"""


class Solution:
    def rectCover(self, n):
        if n < 1:
            return 0
        tmp = [1, 1]
        for i in range(2, n+1):
            tmp[i % 2] = tmp[0] + tmp[1]
        return tmp[n % 2]
