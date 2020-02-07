"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

"""


class Solution:
    def rectCover(self, number):
        temp = [0, 1]
        if number == 0:
            return 0
        if number >= 1:
            for i in range(1, number+1):
                temp[i % 2 - 1] = temp[0] + temp[1]
        return temp[number % 2 - 1]


if __name__ == '__main__':
    number = 1
    s = Solution()
    res = s.rectCover(number)
    print(res)