def maxProfit(prices):
    # Initialize variables
    min_price = float('inf')  # Track the minimum price seen so far
    max_profit = 0  # Track the maximum profit

    for price in prices:
        # Update the minimum price
        if price < min_price:
            min_price = price
        # Calculate the profit and update the maximum profit
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5 (Buy on day 2, Sell on day 5)
