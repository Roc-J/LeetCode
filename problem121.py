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
        maxPro = 0
        currMix = prices[0]
        for item in prices[1:]:
            if item - currMix > maxPro:
                maxPro = item - currMix
            if item < currMix:
                currMix = item
        return maxPro

if __name__ == '__main__':
    print Solution().maxProfit([2, 8, 1, 6, 4, 3, 1])