"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

类似：LeetCode 46、17

"""


class Solution:
    def Permutation(self, ss):
        """
        可以把该问题看成两部分：
            第一步：选取第一个位置的字符
            第二步：固定第一个字符，求后面字符的全排列

        """
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        # 第一个字符的可选范围为charList
        charList = list(ss)
        charList.sort()

        result = []

        for i in range(len(charList)):
            # 重复字符不考虑
            if i > 0 and charList[i] == charList[i-1]:
                continue
            # 让剩余的字符去做全排列，得到全排列的list
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            # 剩余每种全排列 与第一个字母相加 都是一个新的字符串
            for j in temp:
                result.append(charList[i]+j)

        return result
