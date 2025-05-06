# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self,size):
        self.root = {chr(i + 97): chr(i + 97) for i in range(size)}
        self.rank = {chr(i + 97): 0 for i in range(size)}

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
            elif self.rank[rooty] > self.rank[rootx]:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1
        
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        dsu = UnionFind(26)
        equation = sorted(equations, key=lambda x: "!=" in x)
        for i in range(n):
            eq = list(equation[i])
            print(eq)
            if eq[1] == '=' and eq[2] == '=':
                dsu.union(eq[0],eq[3])
            else:
                if dsu.is_connected(eq[0],eq[3]):
                    return False
        return True