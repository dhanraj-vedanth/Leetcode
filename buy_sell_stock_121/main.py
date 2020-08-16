from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute force approach:
        - iterate through each element (j)
        - iterate through all elements (i) until the first iterator (j)
        - Find the max profit that is attainable
        - Return it
        """
        # max_profit = 0
        # main_iter = 1
        # while (main_iter < len(prices)):
        #     inner_iter = 0
        #     temp_min = None
        #     while(inner_iter < main_iter):
        #         if prices[inner_iter] < prices[main_iter]:
        #             # Found a smaller val, record if this is the smallest!
        #             if temp_min is None or prices[inner_iter] < temp_min:
        #                 temp_min = prices[inner_iter]
        #         inner_iter += 1
        #     if temp_min is not None:
        #         max_profit = max(max_profit, prices[main_iter] - temp_min)
        #     main_iter += 1
        # print(max_profit)

        """
        Approach #2
        - Maintain a min_variable
        - For each iteration of prices
            - If the current value is lesser than the min we 
              already have - update min val
            - If not - calculate difference!
        """
        min_val = float("inf")
        max_profit = 0
        for each_price in prices:
            if each_price < min_val:
                min_val = each_price
            else:
                max_profit = max(max_profit, each_price - min_val)
        return max_profit



