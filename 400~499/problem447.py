#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x1, y1 in points:
            dmap = defaultdict(int)
            for x2, y2 in points:
                dmap[(x2-x1)**2 + (y2-y1)**2] += 1
            for d in dmap:
                ans += dmap[d]*(dmap[d]-1)
        return ans

if __name__ == '__main__':
    print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))