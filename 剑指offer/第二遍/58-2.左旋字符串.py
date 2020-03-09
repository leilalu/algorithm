"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

"""


class Solution:
    def reverseLeftWords(self, s, n):
        if not s:
            return s
        s = list(s)
        length = len(s)
        if n >= length or n <= 0:
            return ''.join(s)

        begin1 = 0
        end1 = n - 1

        begin2 = n
        end2 = length - 1

        def Reverse(begin, end):
            while begin < end:
                s[begin], s[end] = s[end], s[begin]

                begin += 1
                end -= 1

        Reverse(begin1, end1)

        Reverse(begin2, end2)

        Reverse(0, length-1)

        return ''.join(s)


if __name__ == '__main__':
    s = "lrloseumgh"
    k = 6
    res = Solution().reverseLeftWords(s, k)
    print(res)


