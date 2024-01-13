def coin_change(coins, amount):
    # 基本情况
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        # 分割问题，递归调用
        subproblem = coin_change(coins, amount - coin)
        if subproblem != float('inf'):
            min_coins = min(min_coins, 1 + subproblem)

    return min_coins


# 示例用法
coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print("最少需要硬币数量:", result)