#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix

if __name__ == '__main__':
    print(Solution().rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))