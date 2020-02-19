"""
题目描述：

把n个骰子扔在地上，所有骰子朝上的一面的点数之和为s。
输入n，打印出s的所有可能的值出现的概率。

"""


class Solution1:
    # 基于循环求点数, 时间性能好
    def PrintProbability(self, number):
        """
            用两个数组来存储骰子点数的每一个总数出现次数。
            在一次循环中，第一个数组中的第n个数字表示骰子和为n出现的次数。
            在下一次循环中加入一个新的骰子，此时和为n的骰子出现的次数应该等于上一次循环中骰子点数和为n-1，n-2，n-3，n-4，n-5，n-6的次数的总和，
            也就是把另一个数组的第n个数字对应上一个数组的n-1，n-2，n-3，n-4，n-5，n-6的次数的总和。

            同时需要注意的是，每次使用新数组的时候，需要把数组所有位置清零，因为我们对于第n位进行的累加操作，如果之前第n位有数字但不清零的话，会导致结果偏大。
        :param number:
        :return:
        """
        # 检查无效输入
        if number < 1:
            return

        maxVal = 6
        # 定义两个数组
        probStorage = [[], []]
        probStorage[0] = [0] * (maxVal * number + 1)  # + 1 是因为点数和从1开始， 第n个元素表示骰子点数和n出现的次数 最大 6*n
        probStorage[1] = [0] * (maxVal * number + 1)

        flag = 0
        for i in range(1, maxVal + 1):
            probStorage[flag][i] = 1

        for k in range(2, number + 1):  # k 表示第 k 个骰子
            for i in range(k):
                probStorage[1-flag][i] = 0

            for i in range(k, maxVal * k +1):
                probStorage[1-flag][i] = 0
                for j in range(i+1):
                    if j <= maxVal:
                        probStorage[1-flag][i] += probStorage[flag][i-j]

            flag = 1-flag

            # probStorage[1 - flag] = [0] * (maxVal * number + 1)
            # for pCur in range(k, maxVal * k + 1):
            #     diceNum = 1
            #     while diceNum < pCur and diceNum <= maxVal:
            #         probStorage[1 - flag][pCur] += probStorage[flag][pCur - diceNum]
            #         diceNum += 1
            # flag = 1 - flag
        # 计算概率
        total = maxVal ** number
        for i in range(number, maxVal * number + 1):
            ratio = probStorage[flag][i]
            print("{}: {:e}".format(i, ratio))


class Solution2:
    # 基于递归
    def PrintProbability(self, number):
        # 检查无效输入
        if number < 1:
            return
        maxValue = 6
        maxSum = number * maxValue  # 6 * n

        probabilities = [0] * (maxSum - number + 1)  # 定义一个长为 6n - n + 1 的数组用来储存点数和s出现的次数

        def Probability(number, probabilities):
            for i in range(1, maxValue+1):
                getProbability(number, number, i, probabilities)

        def getProbability( original, current, sum, probabilities):
            # 递归出口
            if current == 1:
                probabilities[sum - original] += 1
            else:
                for i in range(1, maxValue + 1):
                    getProbability(original, current - 1, i + sum, probabilities)

        Probability(number, probabilities)

        # 计算概率
        total = pow(maxValue, number)
        for i in range(number, maxSum+1):
            ratio = probabilities[i-number] / total
            print("{}: {:e}".format(i, ratio))


if __name__ == '__main__':
    number = 2
    s = Solution1()
    s.PrintProbability(number)







