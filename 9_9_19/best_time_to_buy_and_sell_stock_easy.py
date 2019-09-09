# Runtime O(n)
# Memory O(1)

def maxProfit(prices):
    max_profit = 0
    if len(prices) == 0:
        return max_profit
    buy = prices[0]
    i = 1
    while i < len(prices):
        profit = prices[i] - buy
        if profit > max_profit:
            max_profit = profit
        else:
            if prices[i] < buy:
                buy = prices[i]
        i += 1
    return max_profit