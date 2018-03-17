#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        result = []
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                result.append(i)

        i = 0
        count = 0
        for item in result:
            while i+1 < item:
                print('tree -->', i)
                count += 1
                i += 2
            i = item + 2
        while i < len(flowerbed):
            print('tree -->', i)
            count += 1
            i += 2
        return count >= n

if __name__ == '__main__':
    print(Solution().canPlaceFlowers([1,0,0,0,1,0,0,0,0], 2))