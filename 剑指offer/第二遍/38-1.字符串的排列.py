"""
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8

"""


class Solution:
    def permutation(self, s):
        if not s:
            return []
        if len(s) == 1:
            return list(s)

        # 确定第一个字符的可选范围
        charList = list(s)
        charList.sort()

        result = []

        for i in range(len(charList)):
            # charList中的重复字符不考虑，因为charList已经排好序了，因此重复字符是相连的
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for j in temp:
                result.append(charList[i] + j)

        return result