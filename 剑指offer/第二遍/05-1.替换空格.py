"""
题目：
请实现一个函数，把字符串中的每个空格都替换成"%20"。
例如，输入"We are happy"，则输出'We%20are%20happy'

"""
import re


def ReplaceBlank1(s):
    if not s:
        return ''

    array = s.split(' ')
    res = ''
    for i in range(len(array)-1):
        res = res + array[i] + '%20'

    res += array[-1]
    return res


def ReplaceBlank2(s):
    if not s:
        return ''
    res = s.replace(' ', '%20')
    return res


def ReplaceBlank3(s):
    if not s:
        return ''
    ret = re.compile(' ')
    res = ret.sub('%20', s)
    return res


def ReplaceBlank4(s):
    if not s:
        return ''
    count = s.count(' ')
    s = list(s)
    p1 = len(s) - 1
    s += [-1] * count * 2
    p2 = len(s) - 1

    while 0 <= p1 < p2:
        if s[p1] != ' ':
            s[p2] = s[p1]
            p1 -= 1
            p2 -= 1
        else:
            p1 -= 1
            s[p2] = '0'
            p2 -= 1
            s[p2] = '2'
            p2 -= 1
            s[p2] = '%'
            p2 -= 1

    return ''.join(s)


s = 'We are happy'
res = ReplaceBlank4(s)
print(res)