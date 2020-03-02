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

    n = len(numbers)
    if not set(numbers).issubset(set(range(1, n))):
        return False

    num_set = set()
    for num in numbers:
        if num in num_set:
            duplication[0] = num
            return True
        else:
            num_set.add(num)
    return False


def FindDuplicateNumber2(numbers, duplication):
    """"
        哈希表的数组实现
    """
    if not numbers:
        return False
    n = len(numbers)
    if not set(numbers).issubset(set(range(1, n))):
        return False

    count = [-1] * n
    for i in range(n):
        value = numbers[i]
        if count[value] == -1:
            count[value] = 1
        else:
            duplication[0] = numbers[i]
            return True

    return False


def FindDuplicateNumber3(numbers, duplication):
    """
        二分查找
    """
    if not numbers:
        return False
    n = len(numbers)
    if not set(numbers).issubset(set(range(1, n))):
        return False

    def countRange(numbers, start, end):
        if not numbers:
            return 0
        count = 0
        for i in numbers:
            if start <= i <= end:
                count += 1
        return count

    start = 1
    end = n-1
    while start <= end:
        mid = start + ((end - start) >> 1)

        count = countRange(numbers, start, mid)
        print(count)

        if start == end:
            if count > 1:
                duplication[0] = start
                return True
            else:
                break

        if count > (end - start) + 1:
            end = mid
        else:
            start = mid + 1

    return False


numbers = [1,2,2,3,3,3]
duplication = [0]
res = FindDuplicateNumber3(numbers, duplication)
print(res)
print(duplication)