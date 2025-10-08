def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    hold = [0] * n   
    sold = [0] * n   
    rest = [0] * n   

    hold[0] = -prices[0]
    sold[0] = 0
    rest[0] = 0

    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sold[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sold[i - 1])

    return max(sold[-1], rest[-1])

prices1 = [1, 2, 3, 0, 2]
print("Input:", prices1)
print("Output:", maxProfit(prices1))