"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

"""


# 暴力匹配
class Solution1:
    def longestPalindrome(self, s):
        """"
            根据回文子串的定义，枚举出所有【长度大于等于2】的子串，依次判断他们是否是回文，长度为1的子串不用判断就是最长回文子串。
            在具体实现时，可以只针对【当前得到的最长回文子串长度】的子串进行【回文验证】
            在记录最长回文子串的时候，可以只记录【当前子串的起始位置】和【子串长度】，不必做截取

            时间复杂度是 O(n ^ 3) n为字符串长度，对应三层循环，分别是 枚举字符串的左边界，右边界、判断是否是回文子串
            空间复杂度是O(1)

        """
        # 特判
        size = len(s)
        if size < 2:
            return s

        max_len = 1  # 记录当前最长回文子串的长度
        res = s[0]

        # 枚举所有长度大于等于 2 的子串
        for i in range(size-1):  # 起始位置为0～n-2
            for j in range(i+1, size):  # 终止位置为 i+1 ~ n-1
                # 如果长度大于当前最长的回文子串才进行回文验证，如果验证是回文子串，则记录下来，并且更新最长回文子串长度
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j+1]
        return res

    def __valid(self, s, left, right):
        """"
            验证子串 s[left, right] 是否是 回文子串

        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution2:
    def longestPalindrome(self, s):
        """
            1、定义状态：
                dp[i][j] 表示 子串s[i, j] 是否是回文子串

            2、思考状态转移方程 (分类讨论)
                dp[i][j] = (s[i] == s[j])  and dp[i+1][j-1]

                分析这个状态转移方程：

                    （1）“动态规划”事实上是在填一张二维表格，i 和 j 的关系是 i <= j ，因此，只需要填这张表的上半部分；

                    （2）看到 dp[i + 1][j - 1] 就得考虑边界情况。

                    边界条件是：表达式 [i + 1, j - 1] 不构成区间，即长度严格小于 2，即 j - 1 - (i + 1) + 1 < 2 ，整理得 j - i < 3。

                    这个结论很显然：当子串 s[i, j] 的长度等于 2 或者等于 3 的时候，我其实只需要判断一下头尾两个字符是否相等就可以直接下结论了。

                    如果子串 s[i + 1, j - 1] 只有 1 个字符，即去掉两头，剩下中间部分只有 11 个字符，当然是回文；
                    如果子串 s[i + 1, j - 1] 为空串，那么子串 s[i, j] 一定是回文子串。
                    因此，在 s[i] == s[j] 成立和 j - i < 3 的前提下，直接可以下结论，dp[i][j] = true，否则才执行状态转移。

            3、初始化
                单个字符都是回文子串，因此先把对角线初始化为 1
                即 dp[i][i] = 1

            4、输出
                dp[i][j] = True ，就记录子串的长度和起始位置，没有必要截取
                因此记录时，只需要记录回文子串的【起始位置】和【回文长度】

            注意：总是先得到小子串的回文判定，然后大子串才能参考小子串的判断结果

            思路：在子串右边界 j 逐渐扩大的过程中，枚举左边界可能出现的位置
                 枚举左边界的时候也可以从小到大，也可以从大到小

                每当计算新 dp 值的时候，都一定会参考“左下角”的 dp 值，即 dp[i + 1][j - 1]（i + 1 表示在下边，j - 1 表示在左边）。
                因此，从上到下写，或者从下到上写，都是可以的。


        时间复杂度 O(n^2)
        空间复杂度 O(n^2)

        """

        size = len(s)
        # 当子串长度小于2（为0或1时）一定是最长回文子串
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        # 初始化
        for i in range(size):
            dp[i][i] = True

        # 要先算右边界，因为右边界决定子串的最长长度
        for j in range(1, size):
            # 从上往下写
            for i in range(0, j):
                # 判断两端值是否相等
                if s[i] == s[j]:
                    if j - i < 3:
                        # 里面子串长度小于2 为0 或1，一定是回文子串
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                # 记录子串长度
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start+max_len]


class Solution3:
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = True

        max_len = 1
        start = 0

        for j in range(1, size):
            # 从下往上写
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start+max_len]


if __name__ == '__main__':
    s = "babad"
    res = Solution3().longestPalindrome(s)
    print(res)

