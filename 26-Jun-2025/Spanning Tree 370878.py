# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

import math
import heapq
import sys, threading
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque
input = lambda: sys.stdin.readline().rstrip()
def si():
    return input()
def ii():
    return int(input())
def lsi():
    return input().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))
yn = lambda condition: 'YES' if condition else 'NO'
# =========================================
    
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        elif self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)
def solve():
    n , m =  mi()
    dsu = UnionFind(n+1)
    graph = []
    for _ in range(m):
        arr = li()
        graph.append(arr)
    graph.sort(key = lambda x : x[2])
    # print(graph)
    ans = 0
    for u , v , w in graph:
        if not dsu.connected(u,v):
            dsu.union(u,v)
            ans += w
    print(ans)
    return

  

    

# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()

# =========================================
main()
# if __name__ == '__main__':
#   sys.setrecursionlimit(1 << 30)
#   threading.stack_size(1 << 27)
#   main_thread = threading.Thread(target=main)
#   main_thread.start()
#   main_thread.join()
