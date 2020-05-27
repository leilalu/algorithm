"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

"""


class Solution:
    def reverseLeftWords(self, s, n):
        # 首先判断输入是否合法
        if not s or len(s) <= 0 or n < 1:
            return ''

        length = len(s)
        if n > length:
            return s

        s = list(s)

        # 定义逆序字符串函数
        def reverseList(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        start1 = 0
        end1 = n-1

        start2 = n
        end2 = length-1

        reverseList(start1, end1)
        reverseList(start2, end2)
        reverseList(0, length-1)

        return ''.join(s)


class Solution2:
    def reverseLeftWords(self, s, n):
        length = len(s)
        res = ''

        for i in range(n, length+n):
            res += s[i % length]

        return res


if __name__ == '__main__':
    s = "abcdefg"
    n = 2
    res = Solution().reverseLeftWords(s, n)
    print(res)