"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

"""


class Solution:
    def jumpFloor_1(self, number):
        """
        回溯法

        :param number:
        :return:
        """
        candidates = [1, 2]
        size = len(candidates)
        target = number

        path = []
        res = []

        self._dfs(candidates, size, path, res, target)
        return len(res)

    def _dfs(self, candidates, size, path, res, target):
        if target == 0:
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
        temp = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                temp[(i+1) % 2] = temp[0] + temp[1]
        return temp[(number+1) % 2]


if __name__ == '__main__':
    s = Solution()
    res = s.jumpFloor_2(5)
    print(res)
