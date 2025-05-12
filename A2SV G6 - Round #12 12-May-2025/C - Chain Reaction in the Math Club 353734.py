# Problem: C - Chain Reaction in the Math Club - https://codeforces.com/gym/606404/problem/C

import math
from math import gcd
import sys, threading
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
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
# =========================================

"""
# Note

"""

def solve():
    n, m = mi()
    indeg = [0 for _ in range(n+1)]
    graph = defaultdict(list)
    for _ in range(m):
        u,v = mi()
        indeg[u] += 1
        indeg[v] += 1
        graph[u].append(v)
        graph[v].append(u)

    
    q = deque()
    for i in range(1,n+1):
        if indeg[i] == 1:
            q.append(i)

    group = 0
    while q:
        flag = False
        for _ in range(len(q)):
            node = q.popleft()
            if indeg[node] == 1:
                flag = True
                for nei in graph[node]:
                    indeg[nei] -=1
                    if indeg[nei] == 1:
                        q.append(nei)

        if flag:
            group += 1
    print(group)

        

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
#   main_thread = threading.Thre ad(target=main)
#   main_thread.start()
#   main_thread.join()