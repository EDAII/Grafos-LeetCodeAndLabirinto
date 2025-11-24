from typing import List
from collections import deque
import sys

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        sys.setrecursionlimit(10**7)
        n = len(favorite)
        rev = [[] for _ in range(n)]
        for i, f in enumerate(favorite):
            rev[f].append(i)

        indegree = [0] * n
        for f in favorite:
            indegree[f] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            v = favorite[u]
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

        maxCycle = 0
        visited = [False] * n
        for i in range(n):
            if indegree[i] > 0 and not visited[i]:
                cur = i
                length = 0
                while not visited[cur]:
                    visited[cur] = True
                    cur = favorite[cur]
                    length += 1
                if length > maxCycle:
                    maxCycle = length

        dp = [0] * n

        def dfs(u: int) -> int:
            if dp[u] != 0:
                return dp[u]
            best = 1
            for v in rev[u]:
                if indegree[v] == 0:
                    val = dfs(v) + 1
                    if val > best:
                        best = val
            dp[u] = best
            return best

        sumPairs = 0
        for i in range(n):
            j = favorite[i]
            if favorite[j] == i and i < j:
                lenA = 0
                lenB = 0
                for v in rev[i]:
                    if indegree[v] == 0:
                        val = dfs(v)
                        if val > lenA:
                            lenA = val
                for v in rev[j]:
                    if indegree[v] == 0:
                        val = dfs(v)
                        if val > lenB:
                            lenB = val
                sumPairs += lenA + lenB + 2

        return max(maxCycle, sumPairs)