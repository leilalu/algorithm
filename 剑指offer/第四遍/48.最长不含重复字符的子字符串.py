"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:

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
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        length = len(s)
        dp = [0] * length
        dp[0] = 1

        position = [-1] * 256
        position[ord(s[0])] = 0

        for i in range(1, length):
            if position[ord(s[i])] == -1:
                dp[i] = dp[i-1] + 1
            else:
                last = position[ord(s[i])]
                dist = i - last
                if dist > dp[i-1]:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dist

            position[ord(s[i])] = i

        maxValue = -1
        for i in range(length):
            if dp[i] > maxValue:
                maxValue = dp[i]
        return maxValue
    

if __name__ == '__main__':
    s = "pwwkew"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)

