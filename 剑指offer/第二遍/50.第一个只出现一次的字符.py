"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

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
        if not s:
            return ' '

        char_count = [0] * 256

        for item in s:
            char_count[ord(item)] += 1

        for item in s:
            if char_count[ord(item)] == 1:
                return item

        return ' '


if __name__ == '__main__':
    s = "aabbcc"
    res = Solution().firstUniqChar(s)
    print(res)

