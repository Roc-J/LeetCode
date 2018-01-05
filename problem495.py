#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        result = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration <= timeSeries[i+1]:
                result += duration
            else:
                result += (timeSeries[i+1]-timeSeries[i])
        result += duration

        return result

if __name__ == '__main__':
    print(Solution().findPoisonedDuration([2], 2))