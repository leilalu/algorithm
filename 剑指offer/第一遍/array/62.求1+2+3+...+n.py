"""
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

"""


class Solution:
    def Sum_Solution(self, n):
        """"
            利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。

            如果对n连续进行两次反运算，那么非零的n转换为True，0转换为False，利用这一特性终止递归。

            注意考虑测试用例为0的情况。

        """

        return self.sumN(n)

    def sum0(self, n):
        return 0

    # 利用非0值做两次非运算返回False，0做两次非运算返回True
    def sumN(self, n):
        fun = {False: self.sum0, True: self.sumN}

        return n + fun[not not n](n-1)


class Solution2:
    """
        利用 and 短路的性质

        A and B ：如果A不等于0，那么返回B的值（无论B等于什么）
                  如果A等于0，那么直接返回0，不会再计算B了

        因此可以通过A and B 停止递归循环 0 and self.sumNums(n-1) ，直接返回0，不会再递归调用self.sumNums了

    """
    def sumNums(self, n):
        return n and self.sumNums(n-1)

