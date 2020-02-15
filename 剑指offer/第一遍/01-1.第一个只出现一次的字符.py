"""
题目一：字符串中第一个只出现一次的字符

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写.

"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
            【与字符出现次数】有关，包括【重复】，都要考虑使用哈希表

        :param s:
        :return:
        """
        if not s or len(s) == 0:
            return -1

        item_flag = {}
        for index, item in enumerate(list(s)):
            if item in item_flag:
                item_flag[item] = True
            else:
                item_flag[item] = index

        for key in item_flag:
            if item_flag[key] is not True:
                return item_flag[key]

        return -1


if __name__ == '__main__':
    s = 'google'
    sol = Solution()
    res = sol.FirstNotRepeatingChar(s)
    print(res)

