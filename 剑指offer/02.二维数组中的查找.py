"""
题目描述
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""


class Solution:
    def Find(self, target, array):
        """
            关键点在于，元素向不同方向的移动造成的结果不同：
            从左下角开始，向右移动永远会变大，向上移动永远变小，因此进行元素比较时，元素比target大就向上移动使其变小，元素比target小就向右移动使其变大
            同理，如果从右上角开始也是向下变大，向左变小
            但是如果从左上角开始，不论是向右还是向下都会变大，不能确定移动方向
            
        :param target:
        :param array:
        :return:
        """
        if not array:
            return False
        m = len(array)  # 行数
        n = len(array[0])  # 列数

        # 初始位置
        column = 0
        row = m - 1
        while row >= 0 and column < n:
            if array[row][column] < target:
                column += 1
            elif array[row][column] > target:
                row -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    # array = [[1, 2, 8, 9],
    #          [2, 4, 9, 12],
    #          [4, 7, 10, 13],
    #          [6, 8, 11, 15]]

    array = []
    target = 90
    s = Solution()
    res = s.Find(target, array)
    print(res)

