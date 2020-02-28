"""
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

"""


class Solution:
    def match(self, s, pattern):
        """
            思路：当模式中的第二个字符是“*”时：
                    如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。
                    如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
                        1.模式后移2字符，相当于x*被忽略；
                        2.字符串后移1字符，模式后移2字符，相当于x*匹配一位；
                        3.字符串后移1字符，模式不变，即继续匹配字符下一位，相当于x*匹配多位；

            当模式中的第二个字符不是“*”时：
                如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的部分。
                如果字符串第一个字符和模式中的第一个字符相不匹配，直接返回False。

        """
        # 如果两者都为空字符串，则匹配成功（一定要匹配成功，否则当匹配到最后一位时，s和pattern都是空的）
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 如果模式为空，字符串不为空，则匹配不成功
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if s and (pattern[0] == '.' or s[0] == pattern[0]):
                f1 = self.match(s[1:], pattern)  # 多个  字符串后移1字符，模式不变，即继续匹配字符下一位，相当于x*匹配多位；
                f2 = self.match(s[1:], pattern[2:])  # 一个  字符串后移1字符，模式后移2字符，相当于x*匹配一位；
                f3 = self.match(s, pattern[2:])  # 零个  模式后移2字符，相当于x*被忽略；
                if f1 or f2 or f3:
                    return True
                else:
                    return False
            else:
                return self.match(s, pattern[2:])  # 如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。
        elif s and (pattern[0] == '.' or s[0] == pattern[0]):
            return self.match(s[1:], pattern[1:])
        # 如果字符串为空，模式不为空，但模式长度等于1，或者模式长度大于1但第二个字符不为’*‘，则匹配不成功
        else:
            return False
