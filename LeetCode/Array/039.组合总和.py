"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯法

        :param candidates:
        :param target:
        :return:
        """
        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()

        path = []
        res = []
        self._dfs(candidates, 0, size, path, res, target)
        return res

    def _dfs(self, candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path[:])
            return
        for index in range(begin, size):
            residue = target - candidates[index]

            if residue < 0:
                break
            path.append(candidates[index])
            # 下一层不能比上一层少
            self._dfs(candidates, index, size, path, res, residue)
            # 清空path
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)




