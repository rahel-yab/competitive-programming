# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        curr = [(i, *q) for i, q in enumerate(queries)]
        curr.sort(key=lambda x: x[3])
        dsu = UnionFind(n)
        res = [False] * len(queries)
        i = 0 

        for ind, u, v, limit in curr:
            while i < len(edgeList) and edgeList[i][2] < limit:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[ind] = dsu.connected(u, v)

        return res