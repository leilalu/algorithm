"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

"""


class Solution:
    def jumpFloor_1(self, number):
        """
        回溯法, 会超时

        :param number:
        :return:
        """

        candidates = [1, 2]  # 可以选择的台阶数
        size = len(candidates)
        target = number

        path = []  # 一种跳法
        res = []  # 所有跳法

        self._dfs(candidates, size, path, res, target)
        return res

    def _dfs(self, candidates, size, path, res, target):
        if target == 0:
            # 停止条件
            res.append(path[:])
            return

        for index in range(size):
            residue = target - candidates[index]

            if residue < 0:
                break
            path.append(candidates[index])

            self._dfs(candidates, size, path, res, residue)

            path.pop()

    def jumpFloor_2(self, number):
        """
        不使用回溯法实现跳台阶：
        第n个元素前面的两个数字存在一个temp数组中，每次计算更新这个数组即可。
        可以通过n % 2控制对temp数组的元素进行更新
        :param number:
        :return:
        """
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1) % 2]




if __name__ == '__main__':
    s = Solution()
    res = s.jumpFloor_2(5)
    print(res)