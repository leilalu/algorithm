"""
题目:
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级台阶总共可以有多少次条法

"""


class Solution:
    def Jump(self, number):
        if number < 0:
            return None

        array = [1, 1]
        for i in range(2, number+1):
            array[i % 2] = array[0] + array[1]

        return array[number % 2]

