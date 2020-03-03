"""
题目：
写一个函数，输入n，求斐波那契数列的第n项

"""


def Fibonacci1(n):
    if n < 0:
        # 千万不要加 not n 当n=0时 相当于n=False
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return Fibonacci1(n-1) + Fibonacci1(n-2)


def Fibonacci2(n):
    if n < 0:
        return None

    array = [0, 1]

    for i in range(2, n+1):
        array[i % 2] = array[0] + array[1]

    return array[n % 2]


n = 0
res = Fibonacci2(n)
print(res)