"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[j-1] >= nums[j]:
            j -= 1
        else:
            break
    if j == 0:
        nums.reverse()
        return nums

    i = j-1
    while j < len(nums):
        if nums[j] > nums[i]:
            j += 1
        else:
            break

    nums[i], nums[j-1] = nums[j-1], nums[i]

    j = len(nums)-1
    i += 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return nums



nums = [1,5,8,0,7,6,5,3,1]
nextPermutation(nums)
print(nums)
