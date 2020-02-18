"""
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。

假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        """
            根据所给的压栈序列和弹栈序列，模拟压栈、弹栈的真实情况

            如果下一个弹出的数字刚好是辅助栈栈顶的数字，那么直接弹出；
            如果下一个弹出的数字不在辅助栈栈顶，则把压栈序列pushV中还没有入栈的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶为止
            如果所有数字都压入栈后仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列

        :param pushV:
        :param popV:
        :return:
        """

        stack = []
        while popV:
            # 如果stack的最后一个元素与popV中第一个元素相等，将两个元素都弹出
            if stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            # 如果pushV中有数据，压入stack
            elif pushV:
                stack.append(pushV.pop(0))
            # 所有数字都压入栈了，仍没有找到下一个弹出的数字
            else:
                return False
        return True















