"""
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

"""


class Solution:
    def duplicate_1(self, numbers, duplication):
        # 判断非法输入
        if len(duplication) != numbers:
            return None
        if not duplication:
            return None
        table = set()
        for index, num in enumerate(duplication):
            if num in table:
                duplication[0] = num
                print(duplication[0])
                return True
            else:
                table.add(num)
        return False

    def duplicate_2(self, numbers, duplication):
        i = 0
        while i < numbers:
            if duplication[i] == i:
                i += 1
                continue
            elif duplication[duplication[i]] == duplication[i]:
                duplication[0] = duplication[i]
                return True
            elif duplication[duplication[i]] != duplication[i]:
                temp = duplication[i]
                duplication[i] = duplication[duplication[i]]
                duplication[temp] = temp

        return False


if __name__ == '__main__':
    numbers = 7
    duplication = [2,3,1,0,2,5,3]
    s = Solution()
    res = s.duplicate_2(numbers, duplication)
    print(res)