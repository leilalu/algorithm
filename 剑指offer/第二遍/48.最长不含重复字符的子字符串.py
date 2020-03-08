"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 
示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        curLength = 0  # 在该字符前的最长子串长度
        maxLength = 0

        # 记录每个字符上次出现的位置 (共26个字母)
        position = [-1] * 26

        for index, item in enumerate(list(s)):
            # 该字符上次在字符串中出现的位置
            preIndex = position[ord(item) - ord('a')]
            if preIndex == -1 or index - preIndex > curLength:
                # 说明没出现过
                curLength += 1
            else:
                # 如果该字符出现过，并且在上个最长子串内
                if curLength > maxLength:
                    maxLength = curLength

                curLength = index - preIndex

            # 遇到一个字符，存一个字符的位置
            position[ord(item) - ord('a')] = index

        if curLength > maxLength:
            maxLength = curLength

        return maxLength



