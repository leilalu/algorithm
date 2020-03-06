"""
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

"""


class Solution:
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False

        if len(pattern) > 1 and pattern[1] == '*':
            if s and (s[0] == pattern[0] or pattern[0] == '.'):
                f1 = self.match(s, pattern[2:])
                f2 = self.match(s[1:], pattern[2:])
                f3 = self.match(s[1:], pattern)
                return True if f1 or f2 or f3 else False
            else:
                return self.match(s, pattern[2:])

        elif s and (pattern[0] == s[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        else:
            return False
