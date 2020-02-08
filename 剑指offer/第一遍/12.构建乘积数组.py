"""
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],

其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

"""


class Solution:
    def multiply_1(self, A):
        """
        暴力法

        :param A:
        :return:
        """
        if not A or len(A) <= 0:
            return
        num = len(A)
        B = [1] * num
        for i in range(num):
            for j in range(num):
                if j == i:
                    continue
                else:
                    B[i] = B[i] * A[j]
                    print(B[i])

        return B

    def multiply_2(self, A):
        """
        将B写成一个n*n的矩阵，观察得到一个上三角和下三角，可以分别求得

        需要注意的是，返回数组B的初始化，为[1] * length

        :param A:
        :return:
        """

        if A is None or len(A) <= 0:
            return
        length = len(A)
        B = [1] * length  # 全部初始化为1
        # 从上到下求下三角
        for i in range(1, length):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        # 从下到上求上三角
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            B[i] *= temp
        return B


if __name__ == '__main__':
    A = [1,2,3,4]
    s = Solution()
    res = s.multiply_2(A)
    print(res)