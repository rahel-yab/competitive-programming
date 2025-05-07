# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self,x):
        while self.root[x] != x:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = UnionFind(n)
        for i in range(n):
            x1 , y1 = stones[i]
            for j in range(i+1,n):
                x2 , y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    dsu.union(i,j)
        ans = len(set(dsu.find(i) for i in range(n)))
        return n- ans

        # mapx = {}
        # mapy = {}
        # n = len(stones)
        # dsu = UnionFind(n)
        # for i in range(n):
        #     x, y = stones[i]
        #     if x in mapx:
        #         dsu.union(x,mapx[x])
        #     else:
        #         mapx[x] = i
        #     if y in mapy:
        #         dsu.union(y,mapy[y])
        #     else:
        #         mapy[y] = i
        # ans = len(set(dsu.find(i) for i in range(n)))
        # return n - ans
