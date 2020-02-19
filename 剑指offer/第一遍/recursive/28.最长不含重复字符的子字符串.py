"""
题目描述

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
假设字符串中只包含'a'～'z'的字符

例如， 在字符床'arabcacfr'中，最长的不含重复字符的子字符串是'acfr'，长度为4

"""


class Solution:
    def longestSubstring(self, str):
        curLength = 0
        maxLength = 0

        # 记录每个字符上次出现的位置
        position = [-1] * 26
        for index, item in enumerate(list(str)):
            preIndex = position[ord(item) - ord('a')]
            if preIndex < 0 or index - preIndex > curLength:
                curLength += 1
            else:
                if curLength > maxLength:
                    maxLength = curLength

                curLength = index - preIndex

            position[ord(item) - ord('a')] = index

        if curLength > maxLength:
            maxLength = curLength

        return maxLength


if __name__ == '__main__':
    str = 'arabcacfr'
    s = Solution()
    res = s.longestSubstring(str)
    print(res)
