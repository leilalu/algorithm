"""
题目一：字符串中第一个只出现一次的字符

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写.

"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
            【与字符出现次数】有关，包括【重复】，都要考虑使用哈希表

        """

        # 检查无效输入
        if not s:
            return -1

        # 用数组实现一个哈希表，由于字符占8位，共256个字符，因此创建256个
        item_count = [0] * 256
        for item in s:
            item_count[ord(item)] += 1

        for index, item in enumerate(list(s)):
            if item_count[ord(item)] == 1:
                return index

        return -1


if __name__ == '__main__':
    s = 'google'
    sol = Solution()
    res = sol.FirstNotRepeatingChar(s)
    print(res)

