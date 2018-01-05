#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        stack = []
        for item in asteroids:
            flag = 0
            if item < 0:
                if stack == []:
                    result.append(item)
                else:
                    while len(stack) > 0:
                        if stack[-1] < abs(item):
                            stack.pop()
                            continue
                        elif stack[-1] == abs(item):
                            flag = 1
                            stack.pop()
                            break
                        else:
                            flag = 1
                            break
                    if flag == 1:
                        pass
                    else:
                        result.append(item)

            else:
                stack.append(item)
        for item in stack:
            result.append(item)
        return result

if __name__ == '__main__':
    print(Solution().asteroidCollision([-2, -1, 1, 2]))