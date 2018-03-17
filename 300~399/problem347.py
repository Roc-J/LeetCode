#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        resDict = dict()
        for num in nums:
            if num not in resDict:
                resDict[num] = 1
            else:
                resDict[num] += 1
        sortresult = sorted(resDict.items(), key=lambda x: x[1], reverse=True)
        for x in range(k):
            result.append(sortresult[x][0])
        return result

if __name__ == '__main__':
    print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))