def package(n, weight, w):
    # 初始化状态矩阵,n个物品，限制条件是小于w，因此有w+1个值可选
    states = [[0] * (w+1)] * n

    # 第一个状态要单独说
    states[0][0] = 1  # 第0个物品，不放进去
    # 每次放物品之前都要判断有没有超过限制
    if weight[0] <= w:
        states[0][weight[0]] = 1  # 第0个物品，放进去

    for i in range(1, n):
        # 第一种情况：i不放进去，j是放第i个物品时之前的背包重量
        for j in range(0, w+1):
            if states[i-1][j]:
                states[i][i] = 1
        # 只能限制在放入i之前，背包重量j在w-weight[i]，否则加入i，则背包超重
        for j in range(0, w-weight[i]+1):
            if states[i-1][j]:
                states[i][j+weight[i]] = 1

    print(states)

    for i in range(w, -1, -1):
        if states[n-1][i] == 1:
            return i
    return 0


def package_1(n, weight, w):
    # 初始化状态为，所有的可选值
    states = [0] * (w+1)

    # 第一行
    states[0] = 1
    if weight[0] <= w:
        states[weight[0]] = 1

    for i in range(1, n):
        # 如果要把第j个物品放进背包,那么当前背包最大的载重是w-weight[i]，否则放进该物品将会违反限制条件
        for j in range(w-weight[i], -1, -1):
            if states[j]:
                states[j+weight[i]] = 1

    print(states)
    for i in range(w, -1, -1):
        if states[i]:
            return i
    return 0


def package_2(n, weight, w, value):
    states = [[0] * (w+1)] * n

    states[0][0] = 0
    if weight[0] <= w:
        states[0][weight[0]] = value[0]

    for i in range(1, n):
        for j in range(w+1):
            if states[i-1][j]:
                states[i][j] = states[i-1][j]

        for j in range(w-weight[i]+1):
            if states[i-1][j]:
                v = states[i-1][j] + value[i]
                if states[i][j+weight[i]] < v:
                    states[i][j+weight[i]] = v

    print(states)
    maxValue = -1
    for i in range(w, -1, -1):
        if states[n-1][i] > maxValue:
            maxValue = states[n-1][i]
    return maxValue


def package_3(n, weight, w, value):
    states = [0] * (w+1)

    states[0] = 0
    if weight[0] <= w:
        states[weight[0]] = value[0]

    for i in range(1, n):
        for j in range(w-weight[i], -1, -1):
            if states[j]:
                v = states[j] + value[i]
                if v > states[j+weight[i]]:
                    states[j+weight[i]] = v

    print(states)

    maxvalue = -1
    for i in range(w, -1, -1):
        if states[i] > maxvalue:
            maxvalue = states[i]
    return maxvalue


def shoppingCar(n, v, value):
    states = [[0] * (3 * v + 1)] * n
    states[0][0] = 0
    if value[0] <= 3*v:
        states[0][value[0]] = 1

    for i in range(1, n):
        for j in range(3*v + 1):
            if states[i-1][j]:
                states[i][j] = 1

        for j in range(3*v - value[i] + 1):
            if states[i-1][j]:
                states[i][j+value[i]] = 1

    # 打印选择购买哪些产品
    # 找到购买产品最大的金额
    for j in range(v, 3*v+1):
        if states[n-1][j]:
            break
    if j == 3*v+1:
        return

    # 查看n个商品，从最后一个商品开始看
    for i in range(n-1, 0, -1):
        # 如果可达，说明购买了第i个产品
        if j - value[i] >= 0 and states[i-1][j-value[i]]:
            print(value[i])
            j = j - value[i]

    if j != 0:
        print(value[0])

n = 5
value = [3,4,8,9,6]
weight = [2,2,4,6,3]
w = 9
res = package_3(n, weight, w, value)
print(res)



