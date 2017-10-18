'''
Say you have an array for which
the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example
Given array [3,2,3,1,2], return 1.
'''
class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # remember i <= j , it means you can sell and buy stock on same day.
        # find the max profit = max(prices[j] - prices[i]) , j >= i
        if len(prices) == 0:
            return 0

        min_price = float('inf')
        max_profit= 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit


# def main():
#     s = Solution()
#     prices = [3,2,3,1,2]
#     print(s.maxProfit(prices))
#
#     prices = [5,4,3,2,1]
#     print(s.maxProfit(prices))
# 
#
# if __name__ == '__main__':
#     main()
