class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 1. Bottom-up DP, dp[i][j] = dmap[i-1][j] + dmap[i][j-1], O(mn) and O(mn)
        # 2. Combination (m+n-2, m-1)
        dmap = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                l = u = 0
                u = dmap[i-1][j]
                l = dmap[i][j-1]
                dmap[i][j] = l + u
        return dmap[m-1][n-1]
        