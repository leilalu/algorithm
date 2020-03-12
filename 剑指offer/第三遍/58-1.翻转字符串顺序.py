class Solution:
    def reverseWords(self, s):
        if not s or len(s) <= 0:
            return ''

        array = s.split(' ')
        res = ''
        for i in range(len(array)-1, -1, -1):
            if array[i] != '':
                res = res + array[i] + ' '

        return res[:-1]