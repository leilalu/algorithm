"""
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

"""


class Solution:
    def permutation(self, s):
        # 首先判断非法输入
        if not s or len(s) <= 0:
            return []

        # 递归出口
        if len(s) == 1:
            return list(s)

        charList = list(s)
        charList.sort()

        res = []

        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue

            temp = self.permutation(''.join(charList[:i]) + ''.join(charList[i+1:]))
            for j in temp:
                res.append(charList[i] + j)

        return res


if __name__ == '__main__':
    s = "abc"
    res = Solution().permutation(s)
    print(res)

