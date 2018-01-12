#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        resultDict = {}
        for item in strs:
            ls = tuple(sorted(item))
            if not resultDict.has_key(ls):
                resultDict[ls] = []
            resultDict[ls].append(item)
        return resultDict.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))