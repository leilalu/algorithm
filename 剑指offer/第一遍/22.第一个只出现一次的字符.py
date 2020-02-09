"""
题目一：字符串中第一个只出现一次的字符

在字符串中找出第一个只出现一次的字符。
如输入'abaccdeff' 则输出'b'

"""


class Solution:

    # 题目一 字符串中第一个只出现一次的字符
    def FirstNotRepeating_1(self, s):
        """
            首先将字符串转化成一个哈希表，

        :param s:
        :return:
        """

        # 判断输入合法
        if not s or len(s) == 0:
            # 字符串为空
            return None

        num_times = {}

        for item in s:
            if item in num_times:
                num_times[item] += 1
            else:
                num_times[item] = 1

        for item in num_times:
            if num_times[item] == 1:
                # 存在只出现一次的字符
                return item
            else:
                # 不存在只出现一次的字符
                return None


if __name__ == '__main__':
    s = ''
    sol = Solution()
    res = sol.FirstNotRepeating_1(s)
    print(res)

