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
        """
            跳台阶是斐波那契数列的一个应用。怎么看出斐波那契数列？
            我们把n级台阶的跳法看成n的函数f(n)
                当n=1时，f(n) = 1
                当n=2时，f(n) = 2
                当n>2时，第一次跳的时候有两种不同的选择：
                                                一是第一次只跳1级，此跳法剩余n-1级要跳 共f(n-1)种跳法
                                                二是第一次跳2级，此跳法剩余n-2级要跳，共f(n-2)种跳法
                        总计 f(n) = f(n-1) + f(n-2)
                        得到了斐波那契数列
        :param number:
        :return:
        """
        temp = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                temp[(i+1) % 2] = temp[0] + temp[1]
        return temp[(number+1) % 2]


if __name__ == '__main__':
    s = Solution()
    res = s.jumpFloor_2(5)
    print(res)
