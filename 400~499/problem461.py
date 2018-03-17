# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        str1 = bin(x).replace('0b', '')
        str2 = bin(y).replace('0b', '')
        length1 = int(len(str1))
        length2 = int(len(str2))
        if length1 < length2:
            str1 = '0'*(length2-length1) + str1
        else:
            str2 = '0'*(length1-length2) + str2
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count

if __name__ == '__main__':
    print Solution().hammingDistance(1, 5)
