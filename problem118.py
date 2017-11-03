# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, numRows+1):
            if i < 3:
                item = []
                for j in range(i):
                    item.append(1)
                result.append(item)
            else:
                item = [1] * i
                for j in range(1, i-1):
                    item[j] = result[i-2][j-1]+result[i-2][j]
                result.append(item)
        return result

if __name__ == '__main__':
    print Solution().generate(10)


