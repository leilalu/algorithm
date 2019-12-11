"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

"""


class Solution:
    def __init__(self):
        """
        需要两个栈Stack1和Stack2

        """
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        """
            push的时候直接push进Stack1。

        :param node:
        :return:
        """
        self.stack1.append(node)

    def pop(self):
        """
         pop需要判断Stack1和Stack2中元素的情况，
         Stack1空的话，直接从Stack2 pop，Stack1不空的话，把Stack1的元素push进入Stack2，然后pop Stack2的值

        :return:
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            # 如果两个栈均空，说明没有元素，返回None
            return
        elif len(self.stack2) == 0:
            # 如果Stack2空，Stack1不空，将Stack1中的元素push进Stack2
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        # 只要Stack2不空，不管Stack1空不空，都从Stack1中pop
        return self.stack2.pop()


if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    s.pop()
    s.pop()
    s.pop()
    res = s.pop()
    print(res)

