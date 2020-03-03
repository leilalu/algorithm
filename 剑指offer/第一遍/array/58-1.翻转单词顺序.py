""""
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

"""


class Solution1:
    def ReverseSentence(self, s):
        if not s:
            return ''

        array = s.split(' ')

        res = ''
        for i in range(len(array)-1, -1, -1):
            res = res + array[i] + ' '

        return res[:-1]


class Solution2:
    def ReverseSentence(self, s):
        """"
            先翻转整个句子，再翻转句子中的单词

        """
        if not s:
            return ''
        s = list(s)
        begin = 0
        end = len(s) - 1

        def Reverse(begin, end):
            """"
                翻转字符串中的一段（begin 到 end）
            """
            while begin < end:
                # 头尾交换
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1

        # 翻转整个句子
        Reverse(begin, end)

        # 翻转句子中的每个单词
        begin = end = 0
        while begin < len(s)-1:
            if s[begin] == ' ':
                begin += 1
                end += 1
            elif end == len(s) or s[end] == ' ':
                end -= 1
                Reverse(begin, end)
                end += 1
                begin = end

            else:
                end += 1

        return ''.join(s)


if __name__ == '__main__':
    s = 'I am a student.'
    res = Solution2().ReverseSentence(s)
    print(res)
