"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "

"""


class Solution:
    def firstUniqChar(self, s):
        if not s or len(s) <= 0:
            return ' '
        char_num = [0] * 256
        for item in s:
            char_num[ord(item)] += 1

        for item in s:
            if char_num[ord(item)] == 1:
                return item
        return ' '

