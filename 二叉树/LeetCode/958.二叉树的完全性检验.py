"""

给定一个二叉树，确定它是否是一个完全二叉树。

百度百科中对完全二叉树的定义如下：

若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，
第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）

示例 1：
输入：[1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。

示例 2：

输入：[1,2,3,4,5,null,7]
输出：false
解释：值为 7 的结点没有尽可能靠向左侧。

"""


class Solution:
    def isCompleteTree(self, root):
        from collections import deque
        queue = deque([root])
        has_none = False  # 需要一个标志记录是否出现过空

        while queue:
            node = queue.popleft()
            # 如果当前结点为空，且之前没有出现过空，则是第一个空，允许，可以是最后一行
            if not has_none and not node:
                # 第一次出现空
                has_none = True
            # 如果之前出现过空，但是又存在非空结点，说明上一行不满，或者这一行不是全靠左，为False
            elif has_none and node:
                # 之前出现过空，又出现了非空
                return False

            # 如果结点不为空，才将子结点入队，否则没有子结点（这一限制针对的是最后一行的结点）
            if node:
                # 无论左右子结点是否为空，都入队
                queue.extend([node.left, node.right])

        return True













