"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

"""


class Solution:
    def rectCover(self, number):
        """
            矩形覆盖问题仍然是一个斐波那契数列的应用，如何看出是【斐波那契数列】？

            当n=0时，不存在大矩形 f(n) = 0
            当n=1时，只能竖着放 f(n) = 1
            当n>=2时，用第一个2*1的小矩形去覆盖2*n的大矩形的最左边时有两种方法：
                        1）竖着放，右边还剩 2 * (n-1) 的区域 这种情况下有f(n-1)种方法
                        2）横着放在左上角，左下角必须横着放一个小矩形，右边还剩 2 * (n-2) 的区域，这种情况下有f(n-2)种方法
                        总计 f(n) = f(n-1) + f(n-2)

        :param number:
        :return:
        """

        if number == 0:
            return 0

        temp = [1, 1]
        if number >= 2:
            for i in range(2, number+1):
                temp[i % 2] = temp[0] + temp[1]
        return temp[number % 2]


if __name__ == '__main__':
    number = 1
    s = Solution()
    res = s.rectCover(number)
    print(res)