"""
题目二：不修改数组找出重复的数字

在一个【长度为n+1】的数组里的所有数字都在【1～n的范围内】，所以数组中至少有一个数字是重复的。
请找出数组中【任意一个】重复的数字，但不能修改输入的数组。
例如，如果输入长度为8的数组[2,3,5,4,3,2,6,7]，那么对应的输出是重复的数字2或者3

"""


def FindDuplicateNumber1(numbers, duplication):
    """
        哈希表
    """
    if not numbers:
        return False

    if not set(numbers).issubset(set(range(1, len(numbers)))):
        return False

    num_hash = {}
    for i in range(len(numbers)):
        if numbers[i] in num_hash:
            duplication[0] = numbers[i]
            return True
        else:
            num_hash[numbers[i]] = i

    return False


def FindDuplicateNumber2(numbers, duplication):
    """"
        哈希表的数组实现
    """
    if not numbers:
        return False

    if not set(numbers).issubset(set(range(1, len(numbers)))):
        return False

    num_hash = [-1] * len(numbers)

    for num in numbers:
        if num_hash[num] == -1:
            num_hash[num] = 1
        else:
            duplication[0] = num
            return True
    return False


def FindDuplicateNumber3(numbers, duplication):
    """
        二分查找
    """
    if not numbers:
        return False
    if not set(numbers).issubset(set(range(1, len(numbers)))):
        return False

    start = 1
    end = len(numbers) - 1

    while start <= end:
        mid = start + ((end - start) >> 1)
        count = countRange(numbers, start, mid)

        if start == end:
            if count > 1:
                duplication[0] = start
                return True

        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1

    return False


def countRange(numbers, start, end):
    if not numbers:
        return 0
    count = 0
    for num in numbers:
        if start <= num <= end:
            count += 1
    return count


numbers = [2,3,5,4,3,2,6,7]
duplication = [0]
res = FindDuplicateNumber3(numbers, duplication)
print(res)
print(duplication)