# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            string = self.countAndSay(n-1)
            result = ''
            count = 1
            for i in range(len(string)):
                if i < len(string)-1:
                    if string[i] == string[i+1]:
                        count += 1
                    else:
                        result = result + str(count)
                        result += string[i]
                        count = 1
                else:
                    result = result + str(count)
                    result += string[i]
            return result

if __name__ == '__main__':
    print Solution().countAndSay(7)


