from typing import List
import sys

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(10**7)
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i: int, j: int) -> int:
            if dp[i][j] != 0:
                return dp[i][j]
            best = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    val = 1 + dfs(ni, nj)
                    if val > best:
                        best = val
            dp[i][j] = best
            return best
        
        ans = 0
        for i in range(m):
            for j in range(n):
                v = dfs(i, j)
                if v > ans:
                    ans = v
        return ans