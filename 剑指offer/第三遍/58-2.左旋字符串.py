class Solution:
    def reverseLeftWords(self, s, n):
        if not s or len(s) <= 0 or n > len(s):
            return s

        res = ''
        for i in range(n, len(s)+n):
            res += s[i % len(s)]

        return res


if __name__ == '__main__':
    s = 'abcdefg'
    n = 2
    res = Solution().reverseLeftWords(s, n)
    print(res)

