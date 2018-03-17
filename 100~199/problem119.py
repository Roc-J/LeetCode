# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, rowIndex+1):
            if i < 2:
                item = []
                for j in range(i+1):
                    item.append(1)
                result = item
            else:
                item = [1] * (i+1)
                for j in range(1, i):
                    item[j] = result[j - 1] + result[j]
                result = item
        return result


if __name__ == '__main__':
    print Solution().getRow(5)