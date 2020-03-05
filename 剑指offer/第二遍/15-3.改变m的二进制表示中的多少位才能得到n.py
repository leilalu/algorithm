"""

"""


class Solution:
    def ChangeMToN(self, m, n):
        num = m ^ n
        count = 0
        while num:
            count += 1
            num = num & (num-1)
        return count


if __name__ == '__main__':
    m = 10
    n = 13
    s = Solution()
    res = s.ChangeMToN(m, n)
    print(res)