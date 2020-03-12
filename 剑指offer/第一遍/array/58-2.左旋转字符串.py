""""
题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！


字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。

"""


class Solution1:
    def LeftRotateString(self, s, n):
        """"
            可以通过【三次翻转】实现字符串的左旋。
            首先把字符串转化成数组，方便进行字符交换（不转化为数组无法进行交换）
            然后将字符串分为两个部分，0～n-1 和n~length-1 分别找出他们的起始位置和结束位置
            定义一个翻转函数，根据起始位置和结束位置对数组中的元素进行交换

            然后分别调用三次该翻转函数，分别交换第一段、第二段、和全部

            最后返回时别忘了将数组再转换成字符串

        """
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


class Solution2:
    def LeftRotateString(self, s, n):
        """
            可以在字符串后面再复制一个原数组，这样左旋就相当于在两倍的数组上进行滑动
        """
        length = len(s)
        s = s + s
        return s[n:n+length]


class Solution3:
    def LeftRotateString(self, s, n):
        """"
            上一种方法相当于开辟了一个真实的字符串空间，我们可以通过取模计算，模拟开辟了新的空间
        """
        length = len(s)
        res = ''
        for i in range(n, length+n):
            res += s[i % length]
        return res


if __name__ == '__main__':
    s = 'abcdefg'
    n = 2
    res = Solution3().LeftRotateString(s, n)
    print(res)



