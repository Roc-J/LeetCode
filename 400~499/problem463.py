#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        rows, cols = grid.size
        print(rows)
        print(cols)
        if len(grid) == 0:
            return result
        result += sum(list[0])
        result += sum(list[len(grid)-1])
        result += sum(list[:, 0])

if __name__ == '__main__':
    print(Solution().islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))