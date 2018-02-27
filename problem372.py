#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans, pow = 1, a
        for n in b[::-1]:
            ans = (ans * (pow ** n) %1337) % 1337
            pow = (pow ** 10) %1337
        return  ans

if __name__ == '__main__':
    print(Solution().superPow(2, [3, 0, 0]))