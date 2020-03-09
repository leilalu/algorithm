"""

输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。


示例 1：

输入: "the sky is blue"
输出: "blue is sky the"

示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

"""


class Solution1:
    def reverseWords(self, s):
        if not s or len(s) == 0:
            return ''

        array = s.split(' ')
        result = ''
        for i in range(len(array)-1, -1, -1):
            if array[i] == '':
                continue
            result = result + array[i] + ' '

        return result[:-1]


class Solution2:
    def reverseWords(self, s):
        if not s or len(s) == 0:
            return ''

        s = list(s)
        begin = 0
        end = len(s) - 1

        # 翻转字符串
        def Reverse(begin, end):
            while begin < end:
                s[begin], s[end] = s[end], s[begin]

                begin += 1
                end -= 1
        # 翻转整个橘子
        Reverse(begin, end)

        begin = end = 0
        while begin < len(s)-1:
            if s[begin] == ' ':
                begin += 1
                end += 1
            elif s[end] == len(s) or s[end] == ' ':
                end -= 1
                Reverse(begin, end)
                end += 1
                begin = end
            else:
                end += 1

        return ''.join(s)



if __name__ == '__main__':
    s = "a good   example"
    res = Solution2().reverseWords(s)
    print(res)

