"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：

0 <= s 的长度 <= 50000

"""


class Solution:
    def firstUniqChar(self, s):
        # 首先判断输入是否合法
        if not s or len(s) <= 0:
            return ' '

        table = [0] * 256
        for c in s:
            table[ord(c)] += 1

        for c in s:
            if table[ord(c)] == 1:
                return c

        return ' '
