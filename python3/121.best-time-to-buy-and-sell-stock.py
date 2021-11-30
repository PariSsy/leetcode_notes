# Data Structure Study Plan 1
# Day 3
# 121. Best time to buy and sell stock (Easy)
## Four python solutions (brute force, Kadane's algo, comparing w/ min, one-liner) - Solutions 1 to 4
## https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1144842/Several-solutions-in-Python

from typing import List

# (rev 1) find smallest before every element (1052 ms, 68%; 25.2 mb, 12%)
## See solution 4 for a better writing
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        maxProfit = 0
        minPrice = float('inf')
        if len(prices) > 0:
            i = 0
            while i < len(prices):
                if minPrice > prices[i]:
                    minPrice = prices[i]
                else:
                    maxProfit = max(maxProfit, prices[i] - minPrice)
                i += 1
        return maxProfit

# Solution 5, optimal (Runtime 932 ms, 96%; Memory 25.2, 54%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, highest = float('inf'), 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > highest:
                highest = price - minPrice
        return highest


# Solution 4, comparing with min (Runtime 1100 ms, 56%; Memory 25.3 MB, 12%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price, max_profit = float('inf'), 0
        for i in range(n):
            cur = prices[i] - min_price
            max_profit = max(cur, max_profit)
            min_price = min(min_price, prices[i])
        return max_profit
## Time: O(n)
## Space: O(1)


# Solution 3, one-liner (Runtime 1072 ms, 66%; Memory 25.2 MB, 54%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, min_price = 0, float('inf')
        for price in prices:
            res, min_price = max(res, price - min_price), min(min_price, price)
        return res
## Time: O(n)
## Space: O(1)


# Solution 2, Kadane's algorithm (Runtime 1160 ms, 39%; Memory 25.2 MB, 54%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = cur = 0
        for i in range(1,n):
            cur = max(cur + prices[i] - prices[i-1], 0)
            max_profit = max(cur, max_profit)
        return max_profit
## Time: O(n)
## Space: O(1)


# Solution 1, brute force - compare each element, find max diff (runtime limit exceeded)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            for j in range(i+1,n):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit
## Time: O(n^2)
## Space: O(1)