"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


def lengthOfLongestSubstring_1(s: str):

    """

    :param s: 输入字符串
    :return: 无重复字符的最长子串

    方案描述：首先定义最长的子串【LongestSubstring】，初始赋值为【空】，将来每次截取的子串都放在这个变量中；
            然后定义曾经最长子串的长度【max_length】，初始赋值为【0】；
            定义当前子串的开始索引【begin_index】，初始赋值为【0】
            定义当前子串的结束索引【end_index】，初始赋值为【0】；
            当已知字符串长度为0，即字符串【s=""】时，直接返回最大子串的长度为为0
            当字符串长度不为0时，需要遍历字符串：在当前字符s[end_index]不在当前的最长子串中时，将该字符加入最长子串中，
            并更新结束的索引和子串长度、最长子串长度；在当前字符s[end_index]在当前的最长子串中时，需要更新开始索引，向后推进一个字符，
            此时结束索引为开始索引的后一位，并且要更新当前的最长子串为s[begin_index]
            最后当遍历到最后一位时，跳出循环，返回最大子串长度

            这种思想为【滑动窗口】思想

    """

    LongestSubstring = ""
    max_length = 0
    begin_index = 0
    end_index = 0

    if len(s) == 0:
        max_length = 0
    else:
        while(end_index < len(s)):
            if s[end_index] in LongestSubstring:
                begin_index += 1
                end_index = begin_index + 1
                LongestSubstring = s[begin_index]
            else:
                LongestSubstring += s[end_index]
                end_index += 1
                length = end_index - begin_index
                max_length = max(max_length, length)
    return max_length


def lengthOfLongestSubstring_2(s: str):
    """

    :param s: 输入字符串
    :return: 无重复字符的最长子串

    方案描述：当字符串为None或长度为0时，最长子串为0
            当字符串长度不为0时，开始遍历字符串：
                使用一个dict表示字符串所有字符的当前索引，如果当前字符不在当前已遍历的字符中，
                或者在，但是已经超过了当前子串的index，这都不算在当前子串中，此时计算当前子串长度，记录下当前字符的下标；
                如果不当前字符在已遍历的字符中且其下标在当前子串的开始下标之后，意思就是在当前子串中，那么需要子串中与它重复的字符之后开始重新计算，
                不然的话，如果重复的字符在当前子串中间，每次只滑动1个字符的话，会有很长一段时间，当前子串中都有重复的字符。
                如：【aubcdbef】当遇到第二个b时，我们应该把新子串调整到从第一个b之后，不然的话，只在开始下标+1就会出现【ubcdb】这种出现重复字符的当前子串

    """

    if s == None or len(s) == 0:
        return 0
    cur = {}
    start = 0
    max_num = 0
    for i in range(len(s)):
        # s[i]曾出现在子串中，并且上次出现在子串开始或开始之后，则从上次出现开始算
        if s[i] in cur and start <= cur[s[i]]:
            start = cur[s[i]] + 1
        else:
            max_num = max(max_num, i - start + 1)  # 1 2 3
        cur[s[i]] = i
    return max_num


"""
今日收获：
1、子串vs子序列：子串是一个字符串连续的局部，一定是连续的，而子序列可以是不连续的，但是相对位置不能改变。
                如：字符串abcdefg abc是它的子串，abg是它的子序列

2、python的字符串操作：
    1）计算字符串的字符数 用len(str)
    2）python不支持单字符类型，python字符串里的每个字符都是一个字符串，只能通过截取【切片】来获得
    
3、涉及字符串问题时，一定要对【""】和【" "】进行检验，需要注意的是，【""】的长度为0，而【" "】的长度为1

4、本题一个陷阱是，当出现重复字符时，不应该从重复的那个字符开始算新子串，而是要从原子串的后一位开始算！如"dvdf"遇到重复字符【d】，
    新子串不应该从第二个【d】开始了，而是从【v】开始
    
5、注意更新当前子串长度和最大子串长度是在当前字符不在子串中的时候，而不是出现重复字符时。

"""