"""
题目描述

定义一个函数，删除字符串中所有重复出现的字符
例如，输入'google'，删除重复的字符之后的结果是'gole'

"""


class Solution:
    def DeleteChar(self, s):
        # 检查无效输入
        if not s:
            return s
        # 用数组实现一个哈希表 False表示字符串中没有这个字符
        item_flag = [False] * 256

        result = ''
        for item in s:
            if not item_flag[ord(item)]:  # 如果哈希表中没有该字符，说明第一次出现
                result += item
                item_flag[ord(item)] = True

        return result


if __name__ == '__main__':
    str1 = 'google'
    s = Solution()
    res = s.DeleteChar(str1)
    print(res)

