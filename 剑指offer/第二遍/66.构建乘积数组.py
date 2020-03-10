"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

"""


class Solution:
    def constructArr(self, a):
        n = len(a)

        C = [1] * n
        D = [1] * n

        for i in range(1, n):
            C[i] = C[i-1] * a[i-1]
            D[n-i-1] = D[n-i] * a[n-i]

        B = [1] * n
        for i in range(n):
            B[i] = C[i] * D[i]

        return B


if __name__ == '__main__':
    a = [1,2,3,4,5]
    res = Solution().constructArr(a)
    print(res)

















