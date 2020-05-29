import random


def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(max_size)]

"""
插入排序

原理：
    将原始数组分为已排序部分和待排序部分，将待排序部分的第一个元素，插入到已排序部分合适的位置。
    可以有两种策略：
        1）通过不断的比较相邻两元素，若出现逆序则交换，若不逆序则退出
        2）通过向已排序部分的每个元素从尾到头比较，并且对逆序元素进行移动（赋值），当不发生逆序时，则找到插入位置
    第二种策略要比第一种好，因为第一种的交换次数和第二种的移动次数都是数组中存在的逆序数，是相等的，但是交换操作比移动操作的赋值次数要多。
    
执行效率：
    时间复杂度：
        最好情况：O(n)
            输入数据为有序数组，只有比较没有交换，每次与前一个元素进行比较即可，一共比较了n-1次，时间复杂度是O(n)
        最坏情况：O(n*n)
            输入数据为倒序数组，每轮循环都要移动所有的元素，每次移动次数为1+2+3+...+n-1 共n * (n-1) / 2 时间复杂度为O(n*n)
        平均情况：O(n*n)
            在有序数组中插入一个新元素的平均时间复杂度是O(n)
            插入排序相当于循环执行n次插入操作
    
    空间复杂度：
        原地排序：O(1)
    
    稳定性：
        稳定。当遇到值相等的元素时，不进行交换，以确保排序的稳定性

"""

def insert_sort(nums):
    # 不需要进行排序
    if len(nums) < 2:
        return nums

    length = len(nums)
    for i in range(1, length):
        value = nums[i]
        j = i-1  # 与前一个元素相比
        while j >= 0:
            if value < nums[j]:  # 逆序对
                nums[j+1] = nums[j]  # 向后进行数据移动
            else:
                break  # 当遇到小于等于待排元素时，说明找到了位置nums[j] <= nums[i]，那么nums[i]应该填到nums[j]后面nums[j+1]处
            j -= 1

        nums[j+1] = value  # 插入数据

    return nums


if __name__ == '__main__':
    test_time = 10  # 测试100次
    max_size = 10  # 数组最大长度
    max_value = 10  # 数组内元素最大值
    min_value = 0  # 数组内元素最小值
    for i in range(test_time):
        arr1 = get_random_array(max_size, min_value, max_value)  # 随机生成数组
        arr2 = arr1.copy()  # 验证数组
        insert_sort(arr1)  # 对数组排序
        print(arr1)
        if arr1 != sorted(arr2):  # 排序后数组与库函数排序后的数组进行比较
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(arr1))
            break