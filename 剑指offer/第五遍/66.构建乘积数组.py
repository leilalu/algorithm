"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
不能使用除法。

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000

"""


class Solution:
    def constructArr(self, a):
        # 首先判断输入是否合法
        if not a or len(a) <= 0:
            return []

        # 构建两个数组，由于B中元素为连乘，因此C、D中元素初始化为1
        n = len(a)

        C = [1] * n
        D = [1] * n

        for i in range(1, n):
            # C 是从前往后累乘的，D是从后往前累乘的
            C[i] = C[i-1] * a[i-1]  # C[1] = C[0] * a[0]
            D[n-i-1] = D[n-i] * a[n-i]  # D[n-2] = D[n-1] * a[n-1]

        B = [1] * n
        for i in range(n):
            # B[1] = C[1] * D[1]
            B[i] = C[i] * D[i]

        return B


if __name__ == '__main__':
    a = [1,2,3,4,5]
    res = Solution().constructArr(a)
    print(res)