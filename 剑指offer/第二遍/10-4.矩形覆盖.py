"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

"""


class Solution:
    def rectCover(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 0
        array = [1, 1]
        for i in range(2, n+1):
            array[i % 2] = array[0] + array[1]

        return array[n % 2]





