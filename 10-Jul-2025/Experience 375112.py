# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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

# ========================================
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n
        self.val = [0] * n

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] < self.size[rooty]:
                self.root[rootx] = rooty
                self.val[rootx] -= self.val[rooty]
                self.size[rooty] += self.size[rootx]
            else:
                self.root[rooty] = rootx
                self.val[rooty] -= self.val[rootx]
                self.size[rootx] += self.size[rooty]
    def add(self, x, v):
        root = self.find(x)
        self.val[root] += v

    def get(self, x):
        ans = self.val[x]
        while x != self.root[x]:
            x = self.root[x]
            ans += self.val[x]
        return ans

# =========================================
def solve():
    n , m =mi()
    dsu = UnionFind(n+1)
    for _ in range(m):
        arr = list(map(str, input().split()))
        if len(arr) == 3:
            q , x , y = arr[0] , int(arr[1]) , int(arr[2])
        else:
            q , x = arr[0], int(arr[1]) 
        if q == 'join':
            dsu.union(x,y)
        if q == 'get':
            print(dsu.get(x))
        if q == 'add':
            dsu.add(x ,y)
    return
# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()
main()

# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 25)
#     threading.stack_size(1 << 27)
#     thread = threading.Thread(target=main)
#     thread.start()
#     thread.join()
