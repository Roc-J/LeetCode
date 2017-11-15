# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    result.append('%d:%02d' % (h, m))
        return result

if __name__ == '__main__':
    print Solution().readBinaryWatch(4)