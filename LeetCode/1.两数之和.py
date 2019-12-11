"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


# 时间复杂度是O(n^2)
def twoSum_1(nums, target):
    """

    :param nums: 一个整数数组
    :param target: 一个目标值
    :return: list：和为目标值的两个整数的数组下标

    方案描述：这是一种很自然的想法，考虑使用双重循环，每看过一个数，就在剩下的数中找是否存在与其和为目标值的整数,如果存在，则返回他们的下标
            下标用一个list表示，遍历完不存在，则返回None

    优点：思路简单

    缺点：时间复杂度太大，为O(n^2)，整数数组nums的长度很大，算法用时将很长。

    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i]+nums[j]) == target:
                return [i, j]
    return None


# 时间复杂度为O(n):
def twoSum_2(nums, target):
    """

    :param nums:
    :param target:
    :return:

    方案描述：将该问题转化为一个查表操作：找到与某个数和为目标值的数的下标值==>找到该数的下标，因此该题可以通过hashmap解决
            首先构建一个hashmap，由于最后返回的是数的下标，因此构造的hashmap的key为整数数组的元素，即数值，而value则是下标
            接着遍历这个hashmap，先计算出当前值所应该对应的另一个数，然后找这个数在不在hashmap中，如果存在，那么就是找到了，
            返回的是当前的索引和hashmap中记录的另一个数的索引，如果不存在，那么继续下一次循环。
            需要注意的是：返回的一定是当前索引和查表中另一个数的索引，因为当两个数相同时，当前数的索引在hashmap中很有可能已经被覆盖了。

    优点：时间复杂度小，为O(n)

    缺点：空间复杂度高，为O(n)，使用哈希表就是用空间来换时间

    """
    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = i

    for j in range(len(nums)):
        another = target - nums[j]
        if another in d and d[another] != j:
            return [j, d[another]]

# 时间复杂度是O(n)
def twoSum_3(nums, target):
    """

    :param nums:
    :param target:
    :return:

    方案描述：将该问题转化为一个查表操作：找到与某个数和为目标值的数的下标值==>找到该数的下标，因此该题可以通过hashmap解决
            与上述先构建好哈希表再查表的做法不同，这里使用的是【边建表边查找】的方法，使用一次迭代就可以完成。
            首先对整数数组里的每个数，先算出其对应要找的数的值，然后查该数是否在表中，如果不在，那么就把自己写进表中，直到查到了其所需要找的
            数在表中，那么当前的数其实应该在要找的数后面，返回他们两个的索引.这种方法其实在表中始终只有一个数的索引，因此不会出现向上一解法
            中容易出现的误区

    优点：时间复杂度小，为O(n)

    缺点：空间复杂度高，为O(n)，使用哈希表就是用空间来换时间

    """
    d = dict()
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in d:
            return [d[another_num], index]
        d[num] = index

    return None


def twoSum_4(nums, target):
    j = 0
    for i in range(len(nums)):
        if (target - nums[i]) in nums:
            if (nums.count(target-nums[i]) == 1) & ((target - nums[i]) == nums[i]):
                continue
            else:
                j = nums.index(target-nums[i], i+1)
                break

    if j > 0:
        return [i, j]
    else:
        return None

sub = twoSum_4([3,3],6)
print(sub)


# d = [1,2,3,4,3,3]
#
# l = [1,9,0,8]
#
# l.reverse()
#
# print(l)

"""
今日收获：

1、数组list的长度可以用len()函数求得

2、d = dict()可以定义一个新的字典，其长度是0。同理 l = list() 也可以定义一个新的列表，其长度为0

3、list的基本操作有：
    追加元素（在末尾）：l.append(var)
    在指定位置插入元素：l.insert(index,var)
    删除列表中最后一个元素并返回：l.pop()
    删除列表中指定位置的元素并返回：l.pop(index)
    删除列表中第一次出现该元素的元素：l.remove(var)
    该元素在列表中出现的次数：l.count(var)
    追加另一个list，即合并list到l上：l.extend(list) # 不会产生新list，而是加到了原来的l上
    排序(默认从小到大)：l.sort()

4、enumerate函数的作用是为list分配索引，以list为输入，索引起始值可选，
  输出的是list中元素与索引值的key-value对，也就是一个元素为tuple新list
  
5、本题的关键思想是将一个普通的遍历问题转化为查表操作，中间有很多小trick，比如哈希表的建立以值为key，以索引为value，并且还要注意重复的值对
  哈希表的覆盖情况，从而谨慎考虑输出，尽可能用循环的索引代替表中索引。

"""

