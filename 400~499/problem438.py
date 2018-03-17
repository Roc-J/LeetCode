#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        a = []
        l = len(p)
        cp = Counter(p)
        cs = Counter(s[:l - 1])
        i = 0
        while i + l <= len(s):
            cs[s[i + l - 1]] += 1
            if cs == cp:
                a.append(i)
            cs[s[i]] -= 1
            if cs[s[i]] == 0:
                del cs[s[i]]
            i += 1
        return a

if __name__ == '__main__':
    print(Solution().findAnagrams("a","aa"))