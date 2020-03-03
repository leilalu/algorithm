"""
题目一：找出数组中重复的数字
在一个【长度为n】的数组里的所有数字都在【0～n-1的范围内】。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中【任意一个】重复的数字。
例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出是重复的数字2或者3

"""


def FindDuplicateNumber(numbers, duplication):
    if not numbers:
        return False

    for i in range(numbers):
        while numbers[i] != i:
            value = numbers[i]
            if numbers[value] == value:
                duplication[0] = value
                return True
            else:
                numbers[i], numbers[value] = numbers[value], numbers[i]

    return False


























    # # 检查无效输入
    # if not numbers:
    #     return False
    # # 判断数组里的数字都在【0～n-1】之内
    # if not set(numbers).issubset(set(range(len(numbers)))):
    #     return False
    #
    # for i in range(len(numbers)):
    #     while numbers[i] != i:
    #         value = numbers[i]
    #         if numbers[value] == value:
    #             duplication[0] = value
    #             return True
    #         else:
    #             numbers[i], numbers[value] = numbers[value], numbers[i]
    #
    # return False


numbers = [2,3,1,0,2,5,3]
res = FindDuplicateNumber(numbers)
print(res)

