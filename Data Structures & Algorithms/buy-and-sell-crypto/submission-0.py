from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: if there are no prices or only 1 day, cannot make a trade
        if len(prices) < 2:
            return 0

        # Assume we buy on day 1
        lowest_price = prices[0]
        max_profit = 0

        # Check every day starting from day 2
        for price in prices:
            # Case 1: If today's price is cheaper than our previous buy price, update buy price
            if price < lowest_price:
                lowest_price = price

            # Case 2: Otherwise, calculate the profit if we sell today
            else:
                profit_today = price - lowest_price
                if profit_today > max_profit:
                    max_profit = profit_today

        return max_profit