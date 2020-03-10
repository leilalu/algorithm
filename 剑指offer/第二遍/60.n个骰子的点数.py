"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


"""



""""
class Solution {
public:
    vector<double> twoSum(int n) {
        int dp[70];
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= 6; i ++) {
            dp[i] = 1;
        }
        for (int i = 2; i <= n; i ++) {
            for (int j = 6*i; j >= i; j --) {
                dp[j] = 0;
                for (int cur = 1; cur <= 6; cur ++) {
                    if (j - cur < i-1) {
                        break;
                    }
                    dp[j] += dp[j-cur];
                }
            }
        }
        int all = pow(6, n);
        vector<double> ret;
        for (int i = n; i <= 6 * n; i ++) {
            ret.push_back(dp[i] * 1.0 / all);
        }
        return ret;
    }
};

"""


class Solution:
    def twoSum(self, n):
        # 投掷完n个骰子后，各点数出现的次数
        # leetcode上写n最大为11，最大的点数是11* 6 = 66 （每个骰子都投了6），因此开辟一个70的空间，表示各点数出现的次数
        dp = [0] * 70

        # 状态初始化
        # 第一个骰子的点数已知
        for i in range(1, 7):
            dp[i] = 1

        # 剩下的n-1个骰子
        for i in range(2, n+1):
            # 第i个骰子的点数范围是 i ～ 6*i（i是因为前i个骰子都投1， 6*i是因为前i个骰子都投6）
            # 从弟i个骰子的最后一个可能的点数算起，避免重复子结构
            for j in range(6*i, i-1, -1):
                dp[j] = 0
                for cur in range(1, 7):
                    # 当前数的前6个点数相加
                    if j - cur < i-1:
                        # 剩余可相加的数目不足6
                        break
                    dp[j] += dp[j-cur]

        # 所有点数出现的总次数，有n个骰子，每个骰子有6种可能，因此一共是6的n次方次（并不是一共有6的n次方个点数）
        all = pow(6, n)
        res = []
        # 点数的范围是1 * n到6 * n
        for i in range(n, 6*n+1):
            res.append(dp[i] * 1.0 / all)
        return res


if __name__ == '__main__':
    n = 2
    res = Solution().twoSum(n)
    print(res)


