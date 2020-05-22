"""
输入两个整数m和n，计算需要改变m的二进制表示中的多少位才能得到n

"""

"""
两个数的位不同，可以用异或来判断，异或相同为0不同为1，然后统计异或结果中的1 的个数

"""


class Solution:
    def ChangeMToN(self, m, n):
        num = m ^ n
        count = 0
        while num:
            count += 1
            num = (num-1) & num

        return count


if __name__ == '__main__':
    m = 10
    n = 13
    s = Solution()
    res = s.ChangeMToN(m, n)
    print(res)