""""
题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！


字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。

"""


class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return s
        s = list(s)
        length = len(s)

        if n >= length or n <= 0:
            return ''.join(s)

        begin1 = 0
        end1 = n-1

        begin2 = n
        end2 = length-1
        def Reverse(begin, end):
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1

        # 翻转前n个字符
        Reverse(begin1, end1)
        # 翻转后n个字符
        Reverse(begin2, end2)
        # 翻转整个句子
        Reverse(0, length-1)

        return ''.join(s)


if __name__ == '__main__':
    s = 'abcdefg'
    n = 2
    res = Solution().LeftRotateString(s, n)
    print(res)



