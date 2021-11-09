# Data Structure Study Plan 1
# Day 3
# 121. Best time to buy and sell stock (Easy)

from typing import List

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

# Solution 1, brute force - compare each element, find max diff (runtime limit exceeded)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_so_far = 0
        for i in range(n):
            for j in range(i+1,n):
                max_so_far = max(max_so_far, prices[j] - prices[i])
        return max_so_far
## Time: O(n^2)
## Space: O(1)

# Solution 2, Kadane's algorithm (Runtime 1160 ms, 39%; Memory 25.2 MB, 54%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_so_far = cur = 0
        for i in range(1,n):
            cur = max(cur + prices[i] - prices[i-1], 0)
            max_so_far = max(cur, max_so_far)
        return max_so_far
## Time: O(n)
## Space: O(1)

# Solution 3, comparing with min (Runtime 1100 ms, 56%; Memory 25.3 MB, 12%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_so_far, max_so_far = float('inf'), 0
        for i in range(n):
            cur = prices[i] - min_so_far
            max_so_far = max(cur, max_so_far)
            min_so_far = min(min_so_far, prices[i])
        return max_so_far
## Time: O(n)
## Space: O(1)

# Solution 3 one-liner (Runtime 1072 ms, 66%; Memory 25.2 MB, 54%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, min_so_far = 0, float('inf')
        for price in prices:
            res, min_so_far = max(res, price - min_so_far), min(min_so_far, price)
        return res

# Solution 4, similar to solution 3 (Runtime 1076 ms, 65%; Memory 25.1 MB, 54%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit