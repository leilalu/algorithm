"""
计数排序

原理：
    计数排序相当于桶排序的一种特殊情况
    当要排序的n个数据，且所处的范围并不大时，比如最大值是k，我们就可以把数据分成k个桶。【每个桶内的数据值都是相同的】，省掉了桶内排序的时间。

执行效率：
    时间复杂度是O(n+k) k是数据范围

适用场景举例：
    计数排序只能用在数据范围不大的场景中，如果数据范围k要比排序的数据n大得多，就不适合用计数排序了。
    而且计数排序只能给非负整数排序（对应数组的下标），如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数
    举例：如果考生成绩精确到小数后一位，我们就需要将所有的分数都先乘以 10，转化成整数，然后再放到 9010 个桶内。
        再比如，如果要排序的数据中有负数，数据的范围是[-1000, 1000]，那我们就需要先对每个数据都加 1000，转化成非负整数。


    1）高考查分，通过成绩快速排序得到名次
        考生的满分是 900 分，最小是 0 分，这个数据的范围很小，所以我们可以分成 901 个桶，对应分数从 0 分到 900 分。
        根据考生的成绩，我们将这 50 万考生划分到这 901 个桶里。
        桶内的数据都是分数相同的考生，所以并不需要再进行排序。
        我们只需要依次扫描每个桶，将桶内的考生依次输出到一个数组中，就实现了 50 万考生的排序。
        因为只涉及扫描遍历操作，所以时间复杂度是 O(n)。
    2) 给公司员工的年龄排序
        找出公司员工的最大年龄范围，如20～80，这个数据范围很小，我们可以分成61个桶，对应年龄20～80
        根据员工的年龄，将这些员工分到61个桶里
        桶内的数据都是年龄相同的员工，不需要再排序

三、计数排序（Counting sort）
1.算法原理
1）计数其实就是桶排序的一种特殊情况。
2）当要排序的n个数据所处范围并不大时，比如最大值为k，则分成k个桶
3）每个桶内的数据值都是相同的，就省掉了桶内排序的时间。
2.代码实现（参见下一条留言）
案例分析：
假设只有8个考生分数在0-5分之间，成绩存于数组A[8] = [2，5，3，0，2，3，0，3]。
使用大小为6的数组C[6]表示桶，下标对应分数，即0，1，2，3，4，5。
C[6]存储的是考生人数，只需遍历一边考生分数，就可以得到C[6] = [2，0，2，3，0，1]。
对C[6]数组顺序求和则C[6]=[2，2，4，7，7，8]，c[k]存储的是小于等于分数k的考生个数。
数组R[8] = [0，0，2，2，3，3，3，5]存储考生名次。那么如何得到R[8]的呢？
从后到前依次扫描数组A，比如扫描到3时，可以从数组C中取出下标为3的值7，也就是说，到目前为止，包括自己在内，分数小于等于3的考生有7个，也就是说3是数组R的第7个元素（也就是数组R中下标为6的位置）。当3放入数组R后，小于等于3的元素就剩下6个了，相应的C[3]要减1变成6。
以此类推，当扫描到第二个分数为3的考生时，就会把它放入数组R中第6个元素的位置（也就是下标为5的位置）。当扫描完数组A后，数组R内的数据就是按照分数从小到大排列的了。
3.使用条件
1）只能用在数据范围不大的场景中，若数据范围k比要排序的数据n大很多，就不适合用计数排序；
2）计数排序只能给非负整数排序，其他类型需要在不改变相对大小情况下，转换为非负整数；
3）比如如果考试成绩精确到小数后一位，就需要将所有分数乘以10，转换为整数。

"""


# 计数排序，nums为数组，n是数组大小。假设数组中存储的都是非负整数
def counting_sort(nums):
    n = len(nums)
    if n <= 1:  # 无需排序
        return

    # 查找数组中数据的范围
    max = nums[0]
    for i in range(1, n):
        if nums[i] > max:
            max = nums[i]

    # 申请一个计数数组，下标大小[0, max]
    c = [0] * (max+1)  # 下标表示桶，0表示桶内的元素数量初始化为0

    # 计算每个元素的个数，放入c中
    for i in range(n):
        c[nums[i]] += 1

    # c依次累加
    for i in range(1, max+1):
        c[i] += c[i-1]

    # 结果数组
    result = [0] * n
    # 关键步骤
    for i in range(n-1, -1, -1):
        index = c[nums[i]] - 1
        result[index] = nums[i]
        c[nums[i]] -= 1

    # 将结果拷贝给原数组
    for i in range(n):
        nums[i] = result[i]


if __name__ == '__main__':
    nums = [2,5,3,0,2,3,0,3]
    counting_sort(nums)
    print(nums)




