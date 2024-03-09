# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 01:12:48 2024

@author: raghav
"""

class Solution:
    def maxProfit(self, prices):
        print(prices)
        profit = 0
        day = 0
        while day < len(prices):
            val = prices[0]
            print(f"{day} : {prices[day]}")
            index = 1
            while index < len(prices):
                if val < prices[index]:
                   c = prices[index] - val
                   profit = profit + c
                   break
                else:
                   index += 1
            day += 1
        print(profit)
        
        
        
        #print(sorted_prices)
        
        
        
        
     
prices = [7, 1, 5, 3, 6, 4]        
a  = Solution()
a.maxProfit(prices)       
