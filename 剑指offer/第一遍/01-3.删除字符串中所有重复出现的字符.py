"""
题目描述

定义一个函数，删除字符串中所有重复出现的字符
例如，输入'google'，删除重复的字符之后的结果是'gole'

"""


class Solution:
    def DeleteChar(self, s):
        if not s or len(s) <= 1:
            return s
        nums_flag = [False] * 256
        result = ''
        for item in s:
            if not nums_flag[ord(item)]:
                result += item
                nums_flag[ord(item)] = True

        return result


if __name__ == '__main__':
    str1 = 'google'
    s = Solution()
    res = s.DeleteChar(str1)
    print(res)

