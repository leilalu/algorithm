class Solution:
    def sumNums(self, n):
        return self.sumN(n)

    def sumN(self, n):
        func = {True:self.sum0, False:self.sumN}
        return n + func[not n](n-1)

    def sum0(self, n):
        return 0

if __name__ == '__main__':
    n = 0
    res = Solution().sumNums(n)
    print(res)