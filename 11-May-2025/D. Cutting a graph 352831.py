# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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
    
n,m,k = map(int,input().split())
dsu = UnionFind(n+1)
res = []
ans = []
for _ in range(m):
    u,v = map(int,input().split())
    # dsu.union(u,v)
for _ in range(k):
    ques , x ,y = map(str,input().split())
    x = int(x)
    y = int(y)
    res.append([ques,x,y])

ans = []
for ques,x,y in reversed(res):
    if ques == 'ask':
        if dsu.is_connected(x,y):
            ans.append('YES')
        else:
            ans.append('NO')
    else:
        dsu.union(x,y)
for i in reversed(ans):
    print(i)