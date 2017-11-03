# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxP = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] > 0:
                maxP += (prices[i] - prices[i-1])

        return maxP

