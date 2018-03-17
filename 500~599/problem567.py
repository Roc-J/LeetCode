#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        l = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[:l - 1])
        i = 0
        while i + l <= len(s2):
            c2[s2[i + l - 1]] += 1
            if c2 == c1:
                return True
            c2[s2[i]] -= 1
            if c2[s2[i]] == 0:
                del c2[s2[i]]
            i += 1
        return False

if __name__ == '__main__':
    print(Solution().checkInclusion("ab", "eidbyaooo"))