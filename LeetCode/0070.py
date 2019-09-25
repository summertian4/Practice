# -*- coding: utf-8 -*

# 设 f(n) 表示爬阶楼梯的不同方法数，为了爬到第 n 阶楼梯，有两个选择
# · 从第 n-1 阶前进1步
# · 从第 n-2 阶前进2步
# f(n) = f(n - 1) + f(n - 2)

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        
        arr = [i for i in range(n + 1)]

        arr[1] = 1
        arr[2] = 2

        for i in range(3, n + 1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]