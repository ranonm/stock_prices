def stock_prices(prices):
    """
    Accepts an array of stock prices, one for each hypothetical day. 
    It returns a pair of days representing the best day to buy and 
    the best day to sell. Days start at 0.
    """
    max_profit = 0
    for buying_day in range(len(prices)-1):
        for selling_day in range(buying_day + 1, len(prices)):
            profit = prices[selling_day] - prices[buying_day]
            if profit > max_profit:
                max_profit = profit
                best_buying_day = buying_day
                best_selling_day = selling_day
    return [best_buying_day, best_selling_day]
